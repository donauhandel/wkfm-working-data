import os
import glob

files = [os.path.split(x)[-1][5:9] for x in glob.glob("data/editions/*xml")]

for i in range(1, 1946):
    if f"{i:04}" in files:
        pass
    else:
        print(f"wkfm-{i:04}.xml")
