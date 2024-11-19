import glob
import os
import pandas as pd
from acdh_tei_pyutils.tei import TeiReader

img_path = "wmp1-"  # noqa:
files = sorted(glob.glob("./data/editions/*.xml"))
img_list = []
for i, x in enumerate(files, start=1):
    new_name = f"wkfm-{i:04}.xml"
    img_name = f"{img_path}{i:04}.jpg"
    dir, old_name = os.path.split(x)
    doc = TeiReader(x)
    img_list.append(
        {
            "xml": new_name,
            "img_old": doc.any_xpath(".//tei:graphic")[0].attrib["url"],
            "img_new": img_name,
        }
    )
    for u in doc.any_xpath(".//tei:graphic"):
        u.attrib["url"] = img_name
    graphics = doc.any_xpath(".//tei:graphic")
    if len(graphics) > 1:
        graphics[-1].getparent().remove(graphics[-1])
        u.attrib["corresp"] = img_name
    doc.tree_to_file(os.path.join(dir, new_name))

df = pd.DataFrame(img_list)
df.to_csv("img_list.csv", index=False)
