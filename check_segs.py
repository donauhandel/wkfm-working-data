import glob
from acdh_tei_pyutils.tei import TeiReader


files = glob.glob("./data/editions/*.xml")

counter = 0 
for x in files:
    doc = TeiReader(x)
    segs = doc.any_xpath(".//tei:seg[starts-with(@type, 'orighead')]")
    seg_count = len(segs)
    if seg_count == 3:
        pass
    elif seg_count == 5:
        pass
    elif seg_count == 0:
        pass
    else:
        print(x, seg_count)
        counter += 1
print(counter)