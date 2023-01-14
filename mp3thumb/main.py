import os
from root.utils import to_frame, printProgressBar
from PIL import Image
from pydub import AudioSegment
import shutil
from mutagen.mp3 import MP3
from mutagen.id3 import APIC

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))

CONFIG = {
    "width": 48,
    "height": 36,
    "fps": 5,
}

to_frame(CONFIG["width"], CONFIG["height"], CONFIG["fps"], ROOT_PATH)

path = f"{ROOT_PATH}/result"
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)

# TODO: implement multiprocessing
i = 0
printProgressBar(
    i,
    len(os.listdir(f"{ROOT_PATH}/frames")),
    prefix="Progress",
    suffix="Complete",
    length=50,
)
file_count = len(os.listdir(f"{ROOT_PATH}/frames"))
for file in os.listdir(f"{ROOT_PATH}/frames"):
    file_name = os.path.splitext(file)[0]

    # add border to make image square
    img = Image.open(f"{ROOT_PATH}/frames/{file}")
    size = max(CONFIG["width"], CONFIG["height"])
    size = (size, size)
    new_img = Image.new("RGB", size, color="black")
    new_img.paste(
        img, (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
    )
    new_img.save(f"{ROOT_PATH}/frames/{file}")

    # create silent mp3 file
    # TODO: replace with segment of music to each mp3 file
    AudioSegment.silent(duration=1000 / (CONFIG["fps"] * 2)).export(
        f"{ROOT_PATH}/result/{file_name}.mp3", format="mp3"
    )
    # add id3 tag to mp3 file
    audio = MP3(f"{ROOT_PATH}/result/{file_name}.mp3")
    audio.tags.add(
        APIC(
            encoding=3,
            mime="image/png",
            type=3,
            desc="Cover",
            data=open(f"{ROOT_PATH}/frames/{file}", "rb").read(),
        )
    )
    audio.save()
    i += 1
    printProgressBar(
        i,
        file_count,
        prefix="Progress",
        suffix="Complete",
        decimals=2,
        length=80,
    )

# remove frames folder
shutil.rmtree(f"{ROOT_PATH}/frames")
