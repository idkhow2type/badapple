import os
from PIL import Image
from consts import CONSTS
import json

with open('config.json','r') as f:
    global CONFIG
    CONFIG = json.load(f)

code = ""
code += ">" + CONSTS[CONFIG["width"]]
code += ">" + CONSTS[CONFIG["height"]]
code += ">>>>>>"

for i, file in enumerate(os.listdir(f"frames")):
    file = f"frames/{file}"
    image = Image.open(file)
    image = image.convert("L").point(lambda x: 255 if x > 127 else 0, mode="1")

    data = list(image.getdata())
    last_change = 0
    for j, pixel in enumerate(data):
        if j == 0:
            code += ">+" + ("+" if pixel == 0 else "")
        if data[last_change] != pixel:
            code += ">" + CONSTS[j - last_change]
            last_change = j
    code += ">" + CONSTS[len(data) - last_change]

code += ">-<"
with open("data.bf", "w") as f:
    f.write(code)
