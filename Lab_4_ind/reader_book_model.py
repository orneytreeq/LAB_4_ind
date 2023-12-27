import pandas as pd


def get_genres(conn):
 return pd.read_sql('''
 	SELECT * FROM genre
	''', conn)


def get_books(conn, fr, to, genre):
 return pd.read_sql('''
 	SELECT name_author AS "автор", name_genre AS "жанр", price AS "цена" 
	FROM  book JOIN author USING (author_id) JOIN genre USING (genre_id)
	WHERE price BETWEEN '''+str(fr)+''' AND '''+str(to)+''' AND name_genre = "'''+genre+'''"
	''', conn)