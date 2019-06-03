#get_url.py
import xml.etree.ElementTree as ET
import urllib.request

def main(user_ht) :
    e = ET.parse('SearchKindOpenapiList.xml')
    root = e.getroot()

    name_list = []
    for child in root.iter("item") :
        name_list.append(child.findtext("ccbaMnm1"))

    jm_code = ""
    num_code = ""
    sd_code = ""

    for i in name_list:
        if i.find(user_ht) == -1:
            pass
        else : answer = i

    for child in root.iter("item") :
        if child.findtext("ccbaMnm1") == answer:
            jm_code = child.findtext("ccbaKdcd")
            num_code = child.findtext("ccbaAsno")
            sd_code = child.findtext("ccbaCtcd")

    url = "http://www.cha.go.kr/cha/SearchKindOpenapiDt.do?"+"ccbaKdcd="+jm_code+"&ccbaAsno="+num_code+"&ccbaCtcd="+sd_code

    return url





