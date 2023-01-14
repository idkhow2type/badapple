import pyautogui
import pyperclip
import os
import time

CONFIG = {"fps": 5, "targets": ["Messenger"]}

for file in os.listdir("./frames"):
    # very fancy logic to check if active window is a target
    while not any(
        [target in pyautogui.getActiveWindowTitle() for target in CONFIG["targets"]]
    ):
        print('Target not focused')
        time.sleep(0.1)

    # print(file)
    with open(f"./frames/{file}", encoding="utf-8") as f:
        pyperclip.copy(f.read())
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")

    time.sleep(1 / CONFIG["fps"])
