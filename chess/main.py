import os
from PIL import Image
import pyautogui as pag
import pyperclip as ppc

frames = ["" for _ in os.listdir(f"frames")]

for i, file in enumerate(os.listdir(f"frames")):
    file = f"frames/{file}"
    image = Image.open(file)
    image = image.convert("L").point(lambda x: 255 if x > 127 else 0, mode="1")

    # * standard FEN 8x8
    # for j, pixel in enumerate(list(image.getdata())):
    #     frames[i] += "P" if pixel == 255 else "p"
    #     if (j + 1) % 8 == 0:
    #         frames[i] += "/"

    # * chess.com variant
    frames[i] = "R-0,1,0,1-1,1,1,1-1,1,1,1-0,0,0,0-0-{'wb':true,'noCorners':true}-"
    for j, pixel in enumerate(list(image.getdata())):
        frames[i] += ("r" if pixel == 255 else "y") + "Q"
        frames[i] += "/" if (j + 1) % 14 == 0 else ","
    frames[i] = frames[i][:-1]

for frame in frames:
    print(pag.getActiveWindowTitle())
    while "chess" not in pag.getActiveWindowTitle().__str__().lower():
        pass
    print(pag.getActiveWindowTitle())
    # pag.hotkey("ctrl", "a")
    # pag.write(frame)
    # pag.press("enter")
    pag.click(1166, 421)
    pag.hotkey("ctrl", "a")
    ppc.copy(frame)
    pag.hotkey("ctrl", "v")
    pag.click(1083, 550)
