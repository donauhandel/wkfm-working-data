import requests
import glob
from acdh_tei_pyutils.tei import TeiReader

data = requests.get(
    "https://raw.githubusercontent.com/donauhandel/wkfm-transkribus-export/refs/heads/main/imgs.json"
).json()

for x in sorted(glob.glob("./data/editions/*.xml")):
    doc = TeiReader(x)
    graphic = doc.any_xpath(".//tei:graphic")[0]
    url = graphic.attrib["url"].split("_")[-1]
    transkribus_img = data[url]
    graphic.attrib["n"] = transkribus_img
