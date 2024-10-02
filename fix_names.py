import glob
import os
from acdh_tei_pyutils.tei import TeiReader

img_path = "Merkantil_und_Wechselgericht_Merkantilprotokoll_1_Reihe__Reihe_1_7_Protokoll_1_"  # noqa:
files = sorted(glob.glob("./data/editions/*.xml"))
for i, x in enumerate(files, start=1):
    new_name = f"wkfm-{i:04}.xml"
    img_name = f"{img_path}{i:04}.jpg"
    dir, old_name = os.path.split(x)
    doc = TeiReader(x)
    for u in doc.any_xpath(".//tei:graphic"):
        u.attrib["url"] = img_name
    for u in doc.any_xpath(".//tei:pb"):
        u.attrib["corresp"] = img_name
    doc.tree_to_file(new_name)
    print(old_name, new_name, img_name)