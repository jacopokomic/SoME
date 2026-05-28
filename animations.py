import pathlib
import IPython

rendered_videos = {}

def load_existing():
    media_dir = pathlib.Path("media")
    rendered_videos.clear()
    
    for path in media_dir.glob("Cell*.mp4"):
        rendered_videos[path.stem] = path.resolve()

def get_current_cell_index():
    """
    Get a 1-based index of the current cell by looking at unique
    code blocks executed in the notebook history.
    """
    ip = IPython.get_ipython()
    if ip is None:
        return None

    history = ip.user_ns.get("_ih", [])
    if not history:
        return None

    current = history[-1]

    unique_cells = []
    for cell in history:
        if cell.strip() and cell not in unique_cells:
            unique_cells.append(cell)

    if current in unique_cells:
        return unique_cells.index(current) + 1

    return None

def display(result):
    cell_index = get_current_cell_index()
    if cell_index is None:
        return

    scene_name = f"Cell{cell_index - 2}"
    video_path = rendered_videos.get(scene_name)

    if video_path is None:
        return

    try:
        rel_path = video_path.relative_to(pathlib.Path.cwd())
    except Exception:
        rel_path = video_path

    IPython.display.display(IPython.display.HTML(f"""
    <video width="800" autoplay>
        <source src="{rel_path}" type="video/mp4">
    </video>
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