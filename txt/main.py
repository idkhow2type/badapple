import os
import json
from PIL import Image

with open("config.json", "r") as f:
    global CONFIG
    CONFIG = json.load(f)


def reduce_pallete(pixels, palette):
    """
    given pixels and pallete as lists of values from 0 to 255
    pallete is ordered lowest ot highest
    round each pixel value to the nearest pallete value
    """
    return list(
        map(
            lambda pixel: palette[
                min(
                    range(len(palette)),
                    key=list(map(lambda pc: abs(pixel - pc), palette)).__getitem__,
                )
            ],
            pixels,
        )
    )


for file in os.listdir(f"frames"):
    pixels = list(
        map(
            lambda pixel: pixel[0],
            list(Image.open(f"frames/{file}").getdata()),
        )
    )
    pixels = list(
        map(lambda pixel: "░" if pixel else "▓", reduce_pallete(pixels, [0, 255]))
    )
    with open(f"frames/{os.path.splitext(file)[0]}.txt", "w", encoding="utf-8") as f:
        txt = "\n".join(
            [
                "".join(pixels[i : i + CONFIG["width"]])
                for i in range(0, len(pixels), CONFIG["width"])
            ]
        )
        f.write(txt)
    os.remove(f'frames/{file}')
