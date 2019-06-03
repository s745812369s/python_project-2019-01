학과 | 학번 | 성명
---- | ---- | ---- 
사학과 |201704109 |김소윤

## 프로젝트 개요
![기말보고서 흐름도파일](https://github.com/s745812369s/python_project-2019-01/blob/master/%EA%B8%B0%EB%A7%90%EB%B3%B4%EA%B3%A0%EC%84%9C%20%ED%9D%90%EB%A6%84%EB%8F%84%ED%8C%8C%EC%9D%BC.jpg)

1. 한국어/ 중국어/ 영어/ 일본어 중에 언어를 선택받습니다.



2. 한국어를 입력받았다면, 종목별 문화재 리스트, 지역별 문화재 리스트, 문화재 이름 검색의 3가지 항목 중 1개 항목을 선택 받습니다. 

   2-1. 종목별 문화재 리스트 항목을 입력받았다면, 국보, 보물, 사적, 명승, 천연기념물 등의 종목을 선택하는 구문이 나오게 되고, 선택한 항목에 따라      전국에 있는 종목별 문화재 리스트를 보여줍니다. 리스트에 없는 것을 입력 했다면 다시 입력 받습니다.
   
   2-2. 지역별 문화재 리스트 항목을 입력받았다면, 서울, 부산, 경기, 경남, 울산, 대구 등의 지역을 선택하는 구문이 나오게 되고, 선택한 항목에 따라      그 지역에 있는 문화재 리스트를 보여줍니다. 리스트에 없는 것을 입력 했다면 다시 입력 받습니다.
   
   2-3. 문화재 이름 검색 항목을 입력받았다면, 안내받고 싶은 문화재 이름을 입력받고 문화재에 대한 한글 해설(종류, 이름, 위치, 설명)을 출력합니다.
   
   2-3-1. "선택한 언어의 나레이션을 들으시겠습니까? (Y/N)로 대답"에 대한 답을 입력 받고, 대답에 따라 음성을 재생합니다.
   
   2-3-2. "문화재의 이미지를 보시겠습니까? (Y/N)로 대답"에 대한 답을 입력 받고, 대답에 따라 이미지를 보여줍니다.
 
 
 
3. 중국어/ 영어/ 일본어를 선택받았다면, 문화재 이름을 입력받습니다.

   3-1. 입력받은 문화재에 대하여, "선택한 언어의 나레이션을 들으시겠습니까? (Y/N)로 대답"에 대한 답을 입력 받고, 대답에 따라 선택한 언어의 나레이    션 음성을 재생합니다. 

   3-2  입력받은 문화재에 대하여, "문화재의 이미지를 보시겠습니까? (Y/N)로 대답"에 대한 답을 입력 받고, 대답에 따라 이미지를 보여줍니다.


## 사용한 공공데이터 
1. XML 데이터 - SearchKindOpenapiList.xml

   [데이터예시보기](https://github.com/s745812369s/python_project-2019-01/blob/master/SearchKindOpenapiList2.xml)

2. 문화재 상세 검색 Open api 데이터

   [데이터보기](http://www.cha.go.kr/cha/SearchKindOpenapiDt.do?ccbaKdcd=11&ccbaAsno=00030000&ccbaCtcd=11 )

3. 문화재 나레이션  Open api 데이터

   [데이터보기](http://www.cha.go.kr/cha/SearchVoiceOpenapi.do)

## 소스
1. main_choice.py	

   [링크로 소스 내용 보기](https://github.com/s745812369s/python_project-2019-01/blob/master/main_choice.py) 

2. get_url.py

   [링크로 소스 내용 보기](https://github.com/s745812369s/python_project-2019-01/blob/master/get_url.py) 

3. namesearch.py	

   [링크로 소스 내용 보기](https://github.com/s745812369s/python_project-2019-01/blob/master/namesearch.py) 

4. imageprint.py	

   [링크로 소스 내용 보기](https://github.com/s745812369s/python_project-2019-01/blob/master/imageprint.py) 

5. narr.py

   [링크로 소스 내용 보기](https://github.com/s745812369s/python_project-2019-01/blob/master/narr.py)
 
* 참고
[pip install list](https://github.com/s745812369s/python_project-2019-01/blob/master/pip%20install%20list.txt)


* 코드 삽입
~~~python
#main_choice.py
import xml.etree.ElementTree as ET
import get_url
import namesearch
import narr
import imageprint

e = ET.parse('SearchKindOpenapiList.xml')
root = e.getroot()

user_lang = input("한국어/중국어/영어/일본어")
dic_lang = {"한국어":"kr", "영어":"en", "일본어":"jpn", "중국어":"chn"}
language = dic_lang[user_lang]

jm_list = ["국보","보물","사적","명승","천연기념물","국가무형문화재","국가민속문화재"]
jy_list = ["서울", "경기", "인천", "충북", "세종", "충남", "대전", "전북", "광주", "전남", "강원", "경북", "대구", "경남", "울산", "부산"]
if language == "kr":
    user_choice = input("종목별 문화재 리스트/ 지역별 문화재 리스트/ 문화재 이름 검색")
    if user_choice == "종목별 문화재 리스트":
        while True:
            user_jm = input("국보/보물/사적/명승/천연기념물/국가무형문화재/국가민속문화재").replace(" ","")
            if user_jm not in jm_list:
                print("종목을 다시 입력해주세요.")
                continue
            else:
                for child in root.iter("item") :
                    if child.findtext("ccmaName") == user_jm:
                        print(child.findtext("ccmaName")+ " " +child.findtext("crltsnoNm")+" 호"+ " : " +child.findtext("ccbaMnm1"))
                break
    elif user_choice == "지역별 문화재 리스트":
        while True:
            user_jy = input("서울, 경기, 인천, 충북, 세종, 충남, 대전, 전북, 광주, 전남, 강원, 경북, 대구, 경남, 울산, 부산").replace(" ","")
            if user_jy not in jy_list:
                print("지역을 다시 입력해주세요.")
                continue
            else:
                for child in root.iter("item") :
                    if child.findtext("ccbaCtcdNm") == user_jy:
                        print(child.findtext("ccmaName")+ " " +child.findtext("crltsnoNm")+" 호"+ " : "+child.findtext("ccbaMnm1"))
                break

    elif user_choice == "문화재 이름 검색":
        user_ht = input("문화재 이름을 입력해주세요\n"
        +"(지역과 정확한 문화재 명을 함께 입력하면 더 정확한 검색결과를 얻을 수 있습니다.)\n"
        +"Ex) 서울 숭례문,경주 불국사 다보탑")
        url = get_url.main(user_ht)
        namesearch.main(url)

        user_kr_narr = input("선택한 언어의 나레이션을 들으시겠습니까? (Y/N)로 대답").upper()
        if user_kr_narr == "Y":
            narr.main(url, language)
        else : pass

        user_kr_image = input("문화재의 이미지를 보시겠습니까? (Y/N)로 대답").upper()
        if user_kr_narr == "Y":
            imageprint.main(url)
        else : pass
    else:
        print("선택 사항을 다시 입력해주십시오.")

elif language == "en" or language == "jpn" or language == "chn":
    user_ht = input("문화재 이름을 입력해주세요\n"
    +"(지역과 정확한 문화재 명을 함께 입력하면 더 정확한 검색결과를 얻을 수 있습니다.)\n"
    +"Ex) 서울 숭례문,경주 불국사 다보탑")
    url = get_url.main(user_ht)
    user_lang_narr = input("선택한 언어의 나레이션을 들으시겠습니까? (Y/N)로 대답").upper()
    if user_lang_narr == "Y":
        narr.main(url, language)
    else : pass

    user_lang_img = input("문화재의 이미지를 보시겠습니까? (Y/N)로 대답").upper()
    if user_lang_img == "Y":
        imageprint.main(url)
    else : pass

else : print("언어를 다시 선택해주십시오.")
~~~

~~~python
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
~~~

~~~python
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
~~~

~~~python
#imageprint.py
import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
import xml.etree.ElementTree as ET
import urllib.request

def main(url) :
    f = urllib.request.urlopen(url)
    tree = ET.parse(f)
    root1 = tree.getroot()
    f.close()

    for child in root1.iter("item") :
        img_url = child.findtext("imageUrl")

    root = tk.Toplevel()
    response = requests.get(img_url)
    img_data = response.content
    img =Image.open(BytesIO(img_data))
    photo = ImageTk.PhotoImage(img)
    panel = tk.Label(root, image=photo)
    panel.image = photo
    panel.pack(side="bottom", fill="both", expand="yes")
    root.mainloop()
~~~

~~~python
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
~~~




