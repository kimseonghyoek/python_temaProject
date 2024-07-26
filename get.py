import sqlite3
import js

bookData1, bookData2, bookData3, bookData4, bookData5, bookData6 = [], [], [], [], [], []
con, cur = None, None
sql = ""
con = sqlite3.Connection("dbms")
cur = con.cursor()
sql = "select * from YesBook"
try :
    cur.execute(sql)
    while (True):
      row = cur.fetchone()
      if row == None:
          break
      bookData1.append(row[0])
      bookData2.append(row[1])
      bookData3.append(row[2])
      bookData4.append(row[3])
      bookData5.append(row[4])
      bookData6.append(row[5])

    book_list_div = js.document.getElementsByClassName('contents')

    for index in cur:
      num, title, author, introd, price, img_src = row
      book_card = Element('section')
      book_card.className = 'book_card'

      img = Element('img')
      img.className = 'book_img'
      img.setAttribute('src', img_src)
      book_card.appendChild(img)

        # book_text 생성
      book_text = Element('div')
      book_text.className = 'book_text'

      title_element = Element('h3')
      title_element.className = 'book_title'
      title_element.textContent = title
      book_text.appendChild(title_element)
      book_list_div.appendChild(book_card)
      print(sql)
    con.commit()
    con.close()
except Exception as e:
   print(e)
