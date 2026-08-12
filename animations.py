import hashlib
import json
import pathlib
import IPython

rendered_videos = {}

def load_existing():
    rendered_videos.clear()

    for notebook_path in [pathlib.Path("neural-network-self-portrait.ipynb")]:
        try:
            with open(notebook_path, encoding = "utf-8") as f:
                notebook = json.load(f)
        except Exception:
            continue

        code_cells = [c for c in notebook["cells"] if c["cell_type"] == "code"]
        for i, cell in enumerate(code_cells):
            source = "".join(cell["source"]).strip()
            video_path = pathlib.Path("media")/f"Cell{i - 1}.mp4"
            if source and video_path.exists():
                key = hashlib.sha1(source.encode()).hexdigest()
                rendered_videos[key] = video_path.resolve()

def display(result):
    source = getattr(getattr(result, "info", None), "raw_cell", None)
    if source is None:
        ip = IPython.get_ipython()
        history = ip.user_ns.get("_ih", []) if ip is not None else []
        source = history[-1] if history else ""

    key = hashlib.sha1(source.strip().encode()).hexdigest()
    video_path = rendered_videos.get(key)

    if video_path is None:
        return
    scene_name = video_path.stem

    try:
        rel_path = video_path.relative_to(pathlib.Path.cwd())
    except Exception:
        rel_path = video_path

    IPython.display.display(IPython.display.HTML(f"""
        <div id="anim-{scene_name}" style="display: flex; justify-content: center; width: 100%;">
            <video width="800" autoplay muted playsinline style="border-radius: 8px;">
                <source src="{rel_path}" type="video/mp4">
            </video>
        </div>
        <script>
        setTimeout(function() {{
            var el = document.getElementById("anim-{scene_name}");
            if (el) el.scrollIntoView({{ behavior: "smooth", block: "center" }});
        }}, 300);
        </script>
        """))

def generate():
    load_existing()
    ip = IPython.get_ipython()
    if ip is None:
        return

    try:
        ip.events.unregister("post_run_cell", display)
    except ValueError:
        pass

    ip.events.register("post_run_cell", display)

TRACK_HTML = """
<div title="epoch {epoch}/{epochs} - validation AUC {auc:.4f}"
     style="width: 100%; height: 10px; background: var(--border, #e2e8f0); border-radius: 5px; margin: 12px 0 4px 0;">
    <div style="width: {pct:.1%}; height: 100%; background: var(--accent, #3b82f6); border-radius: 5px; transition: width 0.2s ease;"></div>
</div>
"""

track_handle = {"handle": None}

def track():
    ip = IPython.get_ipython()
    if ip is None:
        return
    try:
        epoch = ip.user_ns["epoch"] + 1
        epochs = ip.user_ns["epochs"]
        val_auc = ip.user_ns["val_auc"]
    except KeyError:
        return

    html = IPython.display.HTML(TRACK_HTML.format(epoch = epoch, epochs = epochs, auc = val_auc, pct = epoch/epochs))
    if epoch <= 1 or track_handle["handle"] is None:
        track_handle["handle"] = IPython.display.display(html, display_id = True)
    else:
        track_handle["handle"].update(html)

PREDICT_STYLE = """
<style>
/* No separator line between the code and the widget output */
.jp-Cell-outputWrapper, .jp-OutputArea-child, .jp-OutputArea-output {
    border: none !important;
    margin-top: 0 !important;
    background: transparent !important;
}
.jp-Cell:hover .jp-Cell-inputWrapper,
.jp-Cell:hover .jp-Cell-outputWrapper,
.jp-Cell:hover .jp-OutputArea-child,
.jp-Cell:hover .jp-OutputArea-output,
.jp-Cell:hover .jp-InputArea,
.jp-Cell.jp-mod-active .jp-Cell-outputWrapper {
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
}
.jp-OutputArea-promptOverlay {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}
.prediction-panel {
    margin: 0 auto;
    overflow-x: hidden;
}
.jp-OutputArea-output:has(.prediction-panel),
.prediction-panel .jp-OutputArea-output {
    overflow-x: hidden !important;
}
.prediction-panel .widget-slider,
.prediction-panel .widget-inline-hbox {
    width: 100%;
}
.prediction-panel .widget-label,
.prediction-panel .widget-readout {
    font-family: "JetBrains Mono", "SF Mono", "Cascadia Code", monospace;
    font-size: 14px;
    color: var(--text, #0f172a);
    border: none;
    box-shadow: none;
}
.prediction-panel .noUi-target {
    background: var(--border, #e2e8f0);
    border: none;
    box-shadow: none;
    border-radius: 3px;
}
.prediction-panel .noUi-connect {
    background: var(--accent, #3b82f6);
}
.prediction-panel .noUi-handle {
    background: #ffffff;
    border: 2px solid var(--accent, #3b82f6);
    border-radius: 50%;
    box-shadow: none;
    cursor: pointer;
    transition: border-color 0.2s ease;
}
.prediction-panel .noUi-handle:hover {
    border-color: #2563eb;
}
</style>
"""

PREDICT_RESULT = """
<div style="font-family: 'JetBrains Mono', 'SF Mono', 'Cascadia Code', monospace; font-size: 14px; color: var(--text, #0f172a); padding: 10px 0 6px 0;">
    Estimated probability of serious delinquency within 2 years:
    <b style="color: {color};">{p:.1%}</b>
</div>
<div style="width: 100%; height: 10px; background: var(--border, #e2e8f0); border-radius: 5px;">
    <div style="width: {p:.1%}; height: 100%; background: {color}; border-radius: 5px; transition: width 0.2s ease;"></div>
</div>
"""

def predict():
    import numpy as np
    import ipywidgets as widgets

    ip = IPython.get_ipython()
    if ip is None:
        return
    try:
        prob = ip.user_ns["prob"]
        X_mean = ip.user_ns["X_mean"]
        X_std = ip.user_ns["X_std"]
    except KeyError:
        print("The network is not trained yet - run all the cells above first.")
        return

    style = {"description_width": "220px"}
    layout = widgets.Layout(width = "100%")

    sliders = {
        "age": widgets.IntSlider(value = 40, min = 18, max = 100, description = "Age", style = style, layout = layout),
        "income": widgets.IntSlider(value = 5000, min = 0, max = 30000, step = 100, description = "Monthly income", style = style, layout = layout),
        "debt_ratio": widgets.FloatSlider(value = 0.3, min = 0, max = 2, step = 0.01, description = "Debt ratio", style = style, layout = layout),
        "total_debt": widgets.IntSlider(value = 1500, min = 0, max = 50000, step = 100, description = "Total debt", style = style, layout = layout),
        "utilization": widgets.FloatSlider(value = 0.3, min = 0, max = 1, step = 0.01, description = "Unsecured lines", style = style, layout = layout),
        "credit_lines": widgets.IntSlider(value = 8, min = 0, max = 30, description = "Credit card loans", style = style, layout = layout),
        "real_estate": widgets.IntSlider(value = 1, min = 0, max = 10, description = "Real estate loans", style = style, layout = layout),
        "dependents": widgets.IntSlider(value = 0, min = 0, max = 10, description = "Dependents", style = style, layout = layout),
        "late30": widgets.IntSlider(value = 0, min = 0, max = 20, description = "30-59 days late", style = style, layout = layout),
        "late60": widgets.IntSlider(value = 0, min = 0, max = 20, description = "60-89 days late", style = style, layout = layout),
        "late90": widgets.IntSlider(value = 0, min = 0, max = 20, description = "90+ days late", style = style, layout = layout)
    }

    def estimate(age, income, debt_ratio, total_debt, utilization, credit_lines, real_estate, dependents, late30, late60, late90):
        x = np.array([[
            np.clip(utilization, 0, 1),
            age,
            np.clip(late30, 0, 20),
            np.log1p(debt_ratio),
            np.log1p(income),
            credit_lines,
            np.clip(late90, 0, 20),
            real_estate,
            np.clip(late60, 0, 20),
            dependents,
            np.log1p(total_debt)
        ]])
        x = (x - X_mean)/X_std
        p = prob(x)[0, 0]
        color = "#22c55e" if p < 1/3 else "#f59e0b" if p < 2/3 else "#ef4444"
        IPython.display.display(IPython.display.HTML(PREDICT_RESULT.format(p = p, color = color)))

    out = widgets.interactive_output(estimate, sliders)
    css = widgets.HTML(PREDICT_STYLE)
    panel = widgets.VBox([css] + list(sliders.values()) + [out], layout = widgets.Layout(width = "100%"))
    panel.add_class("prediction-panel")

    IPython.display.display(panel)