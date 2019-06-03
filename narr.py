#narr.py
import xml.etree.ElementTree as ET
import urllib.request
import vlc

def main(url, language) :
    f = urllib.request.urlopen(url)
    tree = ET.parse(f)
    root = tree.getroot()
    f.close()

    jm_code = ""
    num_code = ""
    sd_code = ""
    for child in root.iter("result") :
        jm_code = child.findtext("ccbaKdcd")
        num_code = child.findtext("ccbaAsno")
        sd_code = child.findtext("ccbaCtcd")

    lang = language
    url2 = "http://www.cha.go.kr/cha/SearchVoiceOpenapi.do?"+"ccbaKdcd="+jm_code+"&ccbaAsno="+num_code+"&ccbaCtcd="+sd_code+"&ccbaGbn="+lang
    f = urllib.request.urlopen(url2)
    tree = ET.parse(f)
    root1 = tree.getroot()
    f.close()

    narr_url = ""
    for child in root1.iter("item") :
        narr_url = child.findtext("voiceUrl").replace("\n","").replace("\t","").replace("\r","").replace("  ","")

    p = vlc.MediaPlayer(narr_url)
    p.play()




