import os

import requests
import glob
from acdh_tei_pyutils.tei import TeiReader

os.makedirs("img", exist_ok=True)

images = [os.path.split(x)[-1] for x in sorted(glob.glob("./img/*.jpg"))]
print(images)
print(images)
files = sorted(glob.glob("./data/editions/*xml"))
for x in files:
    f_name = os.path.split(x)[-1].replace(".xml", ".jpg")
    if f_name in images:
        continue
    doc = TeiReader(x)
    url = doc.any_xpath(".//tei:pb[@corresp]/@corresp")[0]
    response = requests.get(url)
    save_path = os.path.join("img", f_name)
    print(f"saving {url} as {f_name}")
    with open(save_path, "wb") as file:
        file.write(response.content)
