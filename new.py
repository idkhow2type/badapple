import argparse
import os
import json
from toframe import to_frame
import shutil


def size_str(string):
    value = string.split("/")

    if len(value) != 2:
        raise argparse.ArgumentTypeError("Value has to be of form <width>/<height>")
    if value[0] == value[1] == ".":
        raise argparse.ArgumentTypeError("Both width and height can't be '.'")

    try:
        if value[0] == ".":
            height = int(value[1])
            value = (int(4 / 3 * height), height)
        elif value[1] == ".":
            width = int(value[0])
            value = (width, int(3 / 4 * width))
        else:
            value = (int(value[0]), int(value[1]))
    except:
        raise argparse.ArgumentTypeError("Width and height must be integers or '.'")

    return value


parser = argparse.ArgumentParser(
    prog="Bad Apple setup", description="A script to help setup new Bad Apple projects"
)
parser.add_argument("name")
parser.add_argument("--size", "-s", type=size_str, default="48/36")
parser.add_argument("--fps", "-f", type=int, default=5)
parser.add_argument("--template", "-t", action='store_true')

args = parser.parse_args()
config = {"width": args.size[0], "height": args.size[1], "fps": args.fps}

os.mkdir(args.name)
with open(f"{args.name}/config.json", "w") as f:
    f.write(json.dumps(config))

to_frame(args.name, config)

if args.template:
    with open(f'{args.name}/main.py','w') as f:
        f.write("""
        """)