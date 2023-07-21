import glob
from acdh_tei_pyutils.tei import TeiReader

files = glob.glob('./data/editions/*xml')
arche_base = "https://id.acdh.oeaw.ac.at/wkfm/"

for x in files:
    doc = TeiReader(x)
    facs_url = doc.any_xpath(".//tei:graphic/@url")[0]
    pb = doc.any_xpath(".//tei:pb")[0]
    pb.attrib["corresp"] = f"{arche_base}{facs_url}"
    doc.tree_to_file(x)