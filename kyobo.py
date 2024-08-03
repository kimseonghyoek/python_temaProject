import sqlite3
import requests
from bs4 import BeautifulSoup

# def yes24_crawler(url):

#     books = []
#     for book in soup.select('.gd_productbox'):
#         title = book.select_one('.gd_name').text.strip()
#         author = book.select_one('.gd_auth').text.strip()
#         price = book.select_one('.gd_price .yes_b').text.strip()
#         # 이미지 URL 등 다른 정보도 필요에 따라 추출
#         books.append({
#             'title': title,
#             'author': author,
#             'price': price,
#             # ...
#         })

#     return books

# # 크롤링 실행 및 결과 출력
# results = yes24_crawler(url)
# print(results)
# for book in results:
#     print(book)

def crawlingYes24BestSeller():
    title = []
    author = []
    price_result = []

    html = "https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber=1&pageSize=24"
    response = requests.get(html)
    soup = BeautifulSoup(response.text, 'html.parser')
    uls = soup.select("#yesBestList")

  # 제목
    for books in uls:
        list_book = books.find_all("a", {"class":"gd_name"})
        for abs in list_book:
            title.append(abs.text)

  # 저자
    for books in uls:
        list_author = books.select("li > div > div.item_info > div.info_row.info_pubGrp > span.authPub.info_auth > a")
        for test in list_author:
            author.append(test.text)

  # 가격
    for books in uls:
        list_price = books.select("li > div > div.item_info > div.info_row.info_price > strong > em")
        for test in list_price:
            price_result.append(test.text)
# 데이터 주입
    con, cur = None, None
    data1, data2, data3, data4, data5, data6 = "", "", "", "", "", ""

    con = sqlite3.Connection("dbms")
    cur = con.cursor()
    introd = "yes24는 없음"
    sql = ""

    for index in range(10):
        data1=index+1;data2=title[index];data3=author[index];data4=introd;data5=price_result[index]
        try :
            sql = "INSERT INTO YesBook (book_num, title, author, introd, price, img_link) VALUES (?, ?, ?, ?, ?, ?)"
            cur.execute(sql, (data1, data2, data3, data4, data5, data6))
        except:
            print(sql)
            print("데이터 주입 실패")
        else:
            print("데이터 주입 완료")
    con.commit()
    con.close()



crawlingYes24BestSeller();
