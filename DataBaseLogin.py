import sqlite3 as lite
import tkinter
from tkinter import messagebox


def create_table(): 
     
 try: 
 # Conectar ao banco de dados SQLite
     conexao = lite.connect("login.db")
     cursor = conexao.cursor()

# Criar uma tabela se não existir
     comando = '''CREATE TABLE IF NOT EXISTS Login(
                     usuario VARCHAR(10) NOT NULL,
                     senha INTEGER NOT NULL,
                     PRIMARY KEY (usuario)
                     );'''
     cursor.execute(comando)
     conexao.commit()
 
 except lite.DatabaseError as err:

     print("Erro de banco de dados", err)
 
 finally:
     
    if conexao:
         cursor.close()
         conexao.close()

def insert_table(usuario, senha):

  try: 
     conexao = lite.connect("login.db")
     cursor = conexao.cursor()

# Add em uma tabela 
     comando = '''INSERT INTO Login( usuario, senha) VALUES (?,?)'''         
     cursor.execute(comando, (usuario, senha))
     conexao.commit()
     messagebox.showinfo (title="register info", message="Conta criada com sucesso!")

  except lite.DatabaseError as err:

     print("Erro de banco de dados", err)
 
  finally:
      
       if conexao:
          cursor.close()
          conexao.close()

def get_cursor():
    conexao = lite.connect("login.db")
    return conexao.cursor()

if __name__ == '__main__':
  create_table()
  print ("conectado ao banco de dados!")
 