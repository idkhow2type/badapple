import os
import re
from shutil import rmtree


def clean(root, delete, ignore):
    try:
        with open(f"{root}/.gitignore", "r") as f:
            content = f.read()

            temp = re.search("(?<=# delete\n)[\S\s]+?(?=\n\n|$)", content)
            if temp != None:
                delete.extend(temp.group().split("\n"))

            temp = re.search("(?<=# ignore\n)[\S\s]+?(?=\n\n)", content)
            if temp != None:
                ignore.extend(temp.group().split("\n"))

    except FileNotFoundError:
        pass

    print(root, delete)
    for item in delete:
        path = f'{root}/{item}'
        if os.path.isdir(path):
            rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)

    for folder in filter(
        lambda d: os.path.isdir(d) and d not in ignore, os.listdir(root)
    ):
        clean(folder, delete[:], ignore[:])


clean("./", [], [".git"])
