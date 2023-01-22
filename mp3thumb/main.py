import os
from PIL import Image
from pydub import AudioSegment
import shutil
from mutagen.mp3 import MP3
from mutagen.id3 import APIC
import json

with open("config.json", "r") as f:
    global CONFIG
    CONFIG = json.load(f)

if os.path.exists("result"):
    shutil.rmtree("result")
os.mkdir("result")

# TODO: implement multiprocessing
file_count = len(os.listdir("frames"))
for i,file in enumerate(os.listdir(f"frames")):
    file_name = os.path.splitext(file)[0]

    # add border to make image square
    img = Image.open(f"frames/{file}")
    size = max(CONFIG["width"], CONFIG["height"])
    size = (size, size)
    new_img = Image.new("RGB", size, color="black")
    new_img.paste(
        img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
    )
    new_img.save(f"frames/{file}")

    # create silent mp3 file
    # TODO: replace with segment of music to each mp3 file
    AudioSegment.silent(duration=1000 / (CONFIG["fps"] * 2)).export(
        f"result/{file_name}.mp3", format="mp3"
    )
    # add id3 tag to mp3 file
    audio = MP3(f"result/{file_name}.mp3")
    audio.tags.add(
        APIC(
            encoding=3,
            mime="image/png",
            type=3,
            desc="Cover",
            data=open(f"frames/{file}", "rb").read(),
        )
    )
    audio.save()
    print(f'Processed {i}/{file_count}',end='\r')
