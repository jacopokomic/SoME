"""Build the GitHub Pages site (docs/) from the executed notebook.

Usage:
    jupyter nbconvert --to notebook --execute NN.ipynb --output NN-executed.ipynb
    python build_docs.py
"""
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).parent
DOCS = ROOT / "docs"

EXTRA_HEAD = """
<style>
/* --- Neural network self portrait: page styling --- */
body {
    background: #ffffff !important;
    display: flex;
    justify-content: center;
}
.jp-Notebook {
    background: #ffffff !important;
    max-width: 980px;
    width: 100%;
    padding: 48px 16px 96px 16px !important;
    box-shadow: none !important;
}
.jp-Cell {
    background: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    border-radius: 12px !important;
    margin-bottom: 24px !important;
    padding: 8px 12px !important;
    box-shadow: none !important;
    transition: border-color 0.2s ease;
}
.jp-Cell:hover {
    border-color: #94a3b8 !important;
}
.jp-MarkdownCell {
    border: none !important;
    padding: 0 4px !important;
}
.jp-InputPrompt, .jp-OutputPrompt {
    display: none !important;
}
.jp-InputArea-editor {
    background: #f8fafc !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 8px !important;
}
.jp-Cell-outputWrapper {
    border: none !important;
    background: transparent !important;
}
.jp-RenderedHTMLCommon {
    font-size: 16px;
    line-height: 1.6;
}
video {
    border-radius: 8px;
    max-width: 100%;
}
</style>
"""

EXTRA_BODY = """
<script>
/* Play each animation when it scrolls into view; pause when it leaves. */
document.addEventListener("DOMContentLoaded", function () {
    var videos = document.querySelectorAll("video");
    videos.forEach(function (v) {
        v.muted = true;
        v.playsInline = true;
        v.preload = "metadata";
        v.removeAttribute("autoplay");
    });
    if (!("IntersectionObserver" in window)) {
        videos.forEach(function (v) { v.play(); });
        return;
    }
    var seen = new WeakSet();
    var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            var v = entry.target;
            if (entry.isIntersecting) {
                if (!seen.has(v)) {
                    seen.add(v);
                    v.currentTime = 0;
                }
                v.play();
            } else {
                v.pause();
            }
        });
    }, { threshold: 0.4 });
    videos.forEach(function (v) { observer.observe(v); });
});
</script>
"""


def main():
    executed = ROOT / "NN-executed.ipynb"
    if not executed.exists():
        sys.exit("NN-executed.ipynb not found - execute the notebook first.")

    DOCS.mkdir(exist_ok=True)

    subprocess.run(
        [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "html",
            str(executed),
            "--output", "index",
            "--output-dir", str(DOCS),
        ],
        check=True,
    )

    html_path = DOCS / "index.html"
    html = html_path.read_text(encoding="utf-8")

    html = re.sub(r"<title>.*?</title>", "<title>Neural network self portrait</title>", html, count=1)
    html = html.replace('src="media\\', 'src="media/')
    html = html.replace("</head>", EXTRA_HEAD + "</head>", 1)
    html = html.replace("</body>", EXTRA_BODY + "</body>", 1)

    html_path.write_text(html, encoding="utf-8")

    media_src = ROOT / "media"
    media_dst = DOCS / "media"
    if media_dst.exists():
        shutil.rmtree(media_dst)
    shutil.copytree(media_src, media_dst)

    print(f"Built {html_path} ({html_path.stat().st_size / 1e6:.1f} MB) + {len(list(media_dst.glob('*.mp4')))} videos")


if __name__ == "__main__":
    main()
