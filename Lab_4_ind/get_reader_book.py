from jinja2 import Template
import sqlite3
from reader_book_model import get_books, get_genres


conn = sqlite3.connect("store.sqlite")
f_damp = open('store.db','r', encoding ='utf-8-sig')
damp = f_damp.read()
f_damp.close()
conn.executescript(damp)
conn.commit()

g = 'Поэзия'
f =400
t = 600



df_books = get_books(conn, f, t, g)
df_genres = get_genres(conn)
print(df_books)
conn.close()

f_template = open('reader_book_templ.html','r', encoding ='utf-8-sig')
html = f_template.read()
f_template.close()
template = Template(html)
result_html = template.render(
	 genre = g,
	 fr = f,
	 to = t,
	 books = df_books,
	 genres = df_genres,
	 len = len
 )

f = open('reader_book.html', 'w', encoding ='utf-8-sig')
f.write(result_html)
f.close()
