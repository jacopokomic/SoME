from manim import config
import scenes
import importlib
import pathlib
import IPython
import time

importlib.reload(scenes)
rendered_videos = {}

def render(an):
    cells = []
    for name in dir(an):
        if name.startswith("Cell"):
            cells.append(name)
    start = time.time()
    for cell in cells:
        config.output_file = cell
        scene_class = getattr(an, cell)
        scene = scene_class()
        scene.render()
        rendered_videos[cell] = scene.renderer.file_writer.movie_file_path
        pct = 100*(cells.index(cell) + 1)/len(cells)
        print("\r" + round(pct)*"|" + (100 - round(pct))*"-" + " " + str(round(pct, 1)) + "%", end = "", flush = True)
    end = time.time()
    print(f"\rgenerated in {round((end - start)//60)} min {round((end - start)%60)} s" + 90*" ", end = "", flush = True)

def display(result):
    exec_count = result.execution_count
    if exec_count is None:
        return
    scene_name = f"Cell{exec_count - 2}"
    if scene_name in rendered_videos:
        video_path = rendered_videos[scene_name]
        rel_path = pathlib.Path(video_path).relative_to(pathlib.Path.cwd())
        IPython.display.display(IPython.display.HTML(f"""
        <video width = "640" autoplay>
            <source src = "{rel_path}" type = "video/mp4">
        </video>
        """))

def generate():
    render(scenes)
    IPython.get_ipython().events.register("post_run_cell", display)