# 교보문고 베스트 셀러 크롤링
from re import I
from typing import OrderedDict
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import sqlite3

# 알라딘 베스트셀러 모으는 함수
def crawlingAladinBestSeller():
    html = urlopen(
        "https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we")
    bsObject = bs(html, "html.parser")
    soup = bsObject.find_all("div", {"class": "ss_book_box"})

    # 이미지 src
    src = []
    for img in soup:
        imgs = img.find_all("img", {"class": "front_cover"})
        for img_src in imgs:
            src.append(img_src.get('src'))

    title = []
    author = []
    price_result = []
    
    for books in soup:
        list_book = books.find_all("li")

        # 책 제목
        title.append(books.find("b").text)

        # 저자
        author_li = list_book[2].text
        temp = author_li.split("(")
        print(temp[0])
        author.append(temp[0])


        # 책 가격
        price = list_book[3].text
        count = price.split(",")
        if len(count) >= 3:
            price_result.append(",".join(count[:3]))
        else:
            price_result.append(price)

    # 데이터 주입
    con, cur = None, None
    data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""

    con = sqlite3.connect("dbms")
    cur = con.cursor()
    introd = "알라딘은 없음"
    sql = ""

    for index in range(10):
        data1=index+1;data2=title[index];data3=author[index];data4=introd;data5=price_result[index];data6=src[index]
        try :
            sql = "INSERT INTO AladinBook (book_num, title, author, introd, price, img_link) VALUES (?, ?, ?, ?, ?, ?)"
            cur.execute(sql, (data1, data2, data3, data4, data5, data6))
        except:
            print(sql)
            print("데이터 주입 실패")
        else:
            print("데이터 주입 완료")
    con.commit()
    con.close()

crawlingAladinBestSeller()