import os
import glob
from acdh_tei_pyutils.tei import TeiReader


files = sorted(glob.glob("./data/editions/*.xml"))
print(len(files))

no_hi_attrib = set()
for x in files:
    f_name = os.path.split(x)[-1]
    doc = TeiReader(x)
    his = doc.any_xpath(".//tei:hi")
    for hi in his:
        if not hi.attrib:
            no_hi_attrib.add(x)
            break

for x in sorted(list(no_hi_attrib)):
    print(x)
print(len(no_hi_attrib), len(files))
