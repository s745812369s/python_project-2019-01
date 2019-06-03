#namesearch.py
import xml.etree.ElementTree as ET
import urllib.request

def main(url) :
    f = urllib.request.urlopen(url)
    tree = ET.parse(f)
    root1 = tree.getroot()
    f.close()

    for child in root1.iter("item") :
        print("=" * 180)
        print("종류 : ", child.findtext("ccmaName"), child.findtext("crltsnoNm"), " 호"  )
        print("이름 : ", child.findtext("ccbaMnm1") )
        if  child.findtext("ccbaCtcdNm") == "기타 ."  :
            pass
        else :
            print("위치 : ", child.findtext("ccbaLcad").replace("\n","").replace("\t","").replace("\r","").replace(" ",""))
            print("설명 : ", child.findtext("content"))



