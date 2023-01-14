import os
import ffmpeg
import argparse
import json
import shutil


def to_frame(name, config):
    if os.path.exists(f'{name}/frames'):
        shutil.rmtree(f'{name}/frames')
    os.mkdir(f'{name}/frames')
    (
        ffmpeg.input("badapple.mp4")
        .filter("fps", fps=config["fps"])
        .filter("scale", width=config["width"], height=config["height"])
        .output(f"{name}/frames/frame%04d.png")
        .overwrite_output()
        .run()
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Bad Apple to frame",
        description="Convert Bad Apple to frame folder using config file",
    )
    parser.add_argument("name")
    name = parser.parse_args().name
    with open(f"{name}/config.json", "r") as f:
        to_frame(name, json.load(f))
