import glob
import lxml.etree as ET
from acdh_tei_pyutils.tei import TeiReader

files = sorted(glob.glob("./data/editions/*.xml"))

for y in files:
    doc = TeiReader(y)
    for x in doc.any_xpath(".//tei:body"):
        ET.strip_tags(x, "{http://www.tei-c.org/ns/1.0}comment")
    doc.tree_to_file(y)
