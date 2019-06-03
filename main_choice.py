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











