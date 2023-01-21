import os
from PIL import Image

for i, file in enumerate(os.listdir("frames")):
    file = f"frames/{file}"
    image = Image.open(file)
    image = image.convert("L").point(lambda x: 255 if x > 127 else 0, mode="1")
