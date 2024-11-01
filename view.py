import sqlite3 as lite

con = lite.connect('pesagem.db')
 
# inserir dados

def inserir_form(i):
   with con: 
       cur = con.cursor()
       query = "INSERT INTO produto (nome, codigo, peso_liquido, data_recebimento, nota_fiscal) VALUES(?,?,?,?,?)"
       cur.execute(query,i)


# Atualizar dados
def atualizar_form(i):
   with con: 
       cur = con.cursor()
       query = "UPDATE produto SET nome=?, codigo=?, Peso_liquido=?, data_recebimento=?, nota_fiscal=? WHERE id=?"
       cur.execute(query,i)


# Deletar dados
def deletar_form(i):
  with con:
      cur = con.cursor()
      query = "DELETE FROM produto WHERE id=?"
      cur.execute(query,i)
 

# Consultar dados
def ver_form():
   ver_dados = []
   with con:
      cur = con.cursor()
      query = "SELECT * FROM produto"
      cur.execute(query)

      rows = cur.fetchall()
      for row in rows:
        ver_dados.append(row)
   return ver_dados
        

# Consultar dados individual
def ver_produto(id):
    ver_dados_individual = []
    with con:
      cur = con.cursor()
      query = "SELECT * FROM produto WHERE id=?"
      cur.execute(query,id)

      rows = cur.fetchall()
      for row in rows:
        ver_dados_individual.append(row)

        

