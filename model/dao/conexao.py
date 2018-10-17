import sqlite3

def conectar():

    SQL = "CREATE TABLE IF NOT EXISTS planeta " \
          "(id INTEGER PRIMARY KEY AUTOINCREMENT ," \
          "nome TEXT NOT NULL," \
          "clima TEXT NOT NULL," \
          "terreno TEXT NOT NULL," \
          "aparicoes NUMERIC)"

    try:

        conexao = sqlite3.connect('model/dao/database.db')
        cursor = conexao.cursor()
        cursor.execute(SQL)
        conexao.commit()
        return conexao

    except sqlite3.Error as error:
        print(error)