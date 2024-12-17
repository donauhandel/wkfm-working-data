# see https://github.com/donauhandel/wkfm-working-data/issues/8

# 2024-12-17

# import glob
# from acdh_tei_pyutils.tei import TeiReader
# from acdh_tei_pyutils.utils import get_xmlid


# for x in sorted(glob.glob("./data/editions/*.xml")):
#     doc = TeiReader(x)
#     graphic = doc.any_xpath(".//tei:graphic")[0]
#     pb = doc.any_xpath(".//tei:pb")[0]

#     f_name = get_xmlid(doc.any_xpath("/tei:TEI")[0]).replace(".xml", ".jpg")
#     transkribus = doc.any_xpath(".//tei:graphic/@n")[0]
#     graphic.attrib["n"] = doc.any_xpath(".//tei:graphic/@url")[0]
#     graphic.attrib["url"] = f"https://id.acdh.oeaw.ac.at/wmp1/{f_name}"

#     pb.attrib["source"] = transkribus
#     bad = doc.any_xpath(".//tei:pb")[0]
#     del bad.attrib["corresp"]
#     doc.tree_to_file(x)
