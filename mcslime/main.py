import os
from PIL import Image
import json
import shutil
from quadtree import QuadTree

with open("config.json", "r") as f:
    global CONFIG
    CONFIG = json.load(f)

if os.path.exists("badappleslime"):
    shutil.rmtree("badappleslime")
os.makedirs("badappleslime/data/badappleslime/functions/draw")
with open("badappleslime/pack.mcmeta", "w") as f:
    f.write(
        '{"pack":{"pack_format": 10,"description": "Plays Bad Apple using slime mobs"}}'
    )
with open("badappleslime/data/badappleslime/functions/play.mcfunction", "w") as f:
    f.writelines(
        [
            "tp @e[tag=Bad_Apple] ~ -999 ~\n",
            "kill @e[tag=Bad_Apple]\n",
            "scoreboard objectives remove frame\n",
            "scoreboard objectives add frame dummy\n",
            "summon marker ~ ~ ~ {Tags: [Bad_Apple]}\n",
            "scoreboard players set @e[type=marker,tag=Bad_Apple] frame 0\n",
            "scoreboard objectives setdisplay sidebar frame\n",
            "function badappleslime:draw/draw0\n",
        ]
    )

code = []
for i, file in enumerate(os.listdir("frames")):
    if i % CONFIG["cutoff"] == 0:
        code.append(
            "tp @e[type=slime,tag=Bad_Apple] ~ -999 ~\ntp @e[type=magma_cube,tag=Bad_Apple] ~ -999 ~\n"
        )
    file = f"frames/{file}"
    image = Image.open(file)
    image = image.convert("L").point(lambda x: 255 if x > 127 else 0, mode="1")
    # image.save(file)

    root = QuadTree(
        0, 0, image.width, image, "root", [], Image.new("L", image.size, "black"), []
    )
    for node in root.color_nodes:
        if node.color == 255 or CONFIG["magma"]:
            code[
                -1
            ] += f"execute as @e[type=marker,tag=Bad_Apple,scores={{frame={i}}}] at @s run summon {'slime' if node.color==255 else 'magma_cube'} ~{node.s/2+node.x} ~{image.width-node.s} ~{node.s/2+node.y} {{NoAI: 1b, Size: {node.s*2-1}, Tags: [Bad_Apple]}}\n"
    print(f"Processed {i+1}/{len(os.listdir('frames'))}", end="\r")

    if i == len(os.listdir("frames")) - 1:
        code[-1] += "scoreboard players add @e[type=marker,tag=Bad_Apple] frame 1\n"
        code[
            -1
        ] += f"execute as @e[type=marker,tag=Bad_Apple,scores={{frame={i//CONFIG['cutoff']}..{i}}}] run schedule function badappleslime:draw/draw{len(code)-1} {1/CONFIG['fps']}s\n"
        with open(
            f"badappleslime/data/badappleslime/functions/draw/draw{i//CONFIG['cutoff']}.mcfunction",
            "w",
        ) as f:
            print
            f.write(code[-1])

for i in range(len(code) - 1):
    code[i] += "scoreboard players add @e[type=marker,tag=Bad_Apple] frame 1\n"
    code[
        i
    ] += f"execute as @e[type=marker,tag=Bad_Apple,scores={{frame={i*CONFIG['cutoff']}..{(i+1)*CONFIG['cutoff']-1}}}] run schedule function badappleslime:draw/draw{i} {1/CONFIG['fps']}s\n"
    code[
        i
    ] += f"execute as @e[type=marker,tag=Bad_Apple,scores={{frame={(i+1)*CONFIG['cutoff']}}}] run schedule function badappleslime:draw/draw{i+1} {1/CONFIG['fps']}s"
    with open(
        f"badappleslime/data/badappleslime/functions/draw/draw{i}.mcfunction", "w"
    ) as f:
        f.write(code[i])
