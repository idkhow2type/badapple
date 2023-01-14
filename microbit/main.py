import os
from PIL import Image

code = ""
for file in os.listdir(f"frames"):
    file = f"frames/{file}"
    image = Image.open(file)
    image = image.convert("L").point(lambda x: 255 if x > 127 else 0, mode="1")

    code += 'basic.show_leds("""\n'
    data = list(image.getdata())
    for i, pixel in enumerate(data):
        code += ("#" if pixel == 255 else ".") + " "
        if (i+1) % 5 == 0:
            code += "\n"
    code += '""")\n'

with open("out.py", "w") as f:
    f.write(code)
