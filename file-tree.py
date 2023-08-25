import argparse
from os.path import isdir, isfile
from pathlib import Path
import os

parser = argparse.ArgumentParser()
parser.add_argument("path")

args = parser.parse_args()
target_dir = Path("C:\\dev\\langs\\py")


if not target_dir.exists():
    print("Doesn't exist")
    raise SystemExit(1)


def make_tree(path, level, connectors, index, parent=None):
    parent_num = None
    if parent:
        parent_num = sum(1 for _ in parent.glob("*"))
    if isdir(path) and isfile(path) == False:
        level += 1
        num = sum(1 for _ in path.glob("*"))
        if parent_num:
            if index == parent_num:
                connectors += "0"
            else:
                connectors += "1"
        else:
            if index == num:
                connectors += "0"
            else:
                connectors += "1"
        x = 0
        for _, entry in enumerate(path.iterdir()):
            if level != 1:
                if x != num - 1:
                    string = ""
                    for i, dig in enumerate(connectors):
                        if i == 0:
                            continue
                        if dig == "0":
                            string += "   "
                        else:
                            string += "│  "
                    else:
                        string += "├──"
                    string += entry.name
                    string += " " + str(connectors)
                    string += f"   {x + 1} / {num}"
                    print(string)

                else:
                    string = ""
                    for i, dig in enumerate(connectors):
                        if i == 0:
                            continue
                        if dig == "0":
                            string += "   "
                        else:
                            string += "│  "
                    else:
                        string += "└──"
                    string += entry.name
                    string += " " + str(connectors)
                    string += f"   {x + 1} / {num}"
                    print(string)

            else:
                if x < num - 1:
                    print(
                        "├──"
                        + entry.name
                        + "  \/  "
                        + str(connectors)
                        + f"   {x + 1} / {num}"
                    )

                else:
                    print(
                        "└──"
                        + entry.name
                        + "  \/  "
                        + str(connectors)
                        + f"   {x + 1} / {num}"
                    )
            x += 1
            make_tree(entry, level, connectors, x, path)


make_tree(target_dir, 0, "", 0)
