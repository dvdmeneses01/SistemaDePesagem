import sqlite3 as lite

con = lite.connect('pesagem.db')

with con:
    cur=con.cursor()
    cur.execute = """CREATE TABLE produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR,
    codigo INT,
    peso_liquido FLOAT,
    data_recebimento DATE,
    nota_fiscal INT)"""
