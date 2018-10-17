import sqlite3
from model.dao import conexao

class PlanetaDAO():

    def __init__(self):

        self.__conn = conexao.conectar()


    def adicionarPlaneta(self, planeta):
        SQL = "INSERT INTO planeta (nome, clima, terreno) VALUES (?,?,?)"

        try:
            cursor = self.__conn.cursor()
            result = cursor.execute(SQL, planeta).rowcount
            self.__conn.commit()
        except sqlite3.Error as error:
            print(error)
        finally:
            self.__conn.close()

        return result


    def adicionarPlanetas(self, planetas):
        SQL = "INSERT INTO planeta (nome, clima, terreno, aparicoes) VALUES (?,?,?,?)"

        try:
            cursor = self.__conn.cursor()
            result = cursor.executemany(SQL, planetas)
            self.__conn.commit()
        except sqlite3.Error as error:
            print(error)
        finally:
            self.__conn.close()

        return result

    def listarPlanetas(self):
        SQL = "SELECT * FROM planeta"
        lstPlanetas = []

        try:
            cursor = self.__conn.cursor()
            results = cursor.execute(SQL).fetchall()
        except sqlite3.Error as error:
            print(error)
        finally:
            self.__conn.close()

        for planeta in results:
            dicPlaneta = {'id': planeta[0], 'nome': planeta[1], 'clima': planeta[2],
                          'terreno': planeta[3], 'aparicoes': planeta[4]}

            lstPlanetas.append(dicPlaneta)

        return {'planetas': lstPlanetas}


    def buscarPorNome(self, nome):
        SQL = "SELECT * FROM planeta WHERE nome = ?"
        pNome = (nome,)
        planeta = None

        try:
            cursor = self.__conn.cursor()
            planeta = cursor.execute(SQL, pNome).fetchone()
        except sqlite3.Error as error:
            print(error)
        finally:
            self.__conn.close()

        if planeta != None:
            planeta = {'id':planeta[0], 'nome':planeta[1], 'clima':planeta[2],
                       'terreno':planeta[3], 'aparicoes':planeta[4]}

        return planeta


    def buscarPorId(self, id):
        SQL = "SELECT * FROM planeta WHERE id = ?"
        pId = (id,)
        planeta = None
        try:
            cursor = self.__conn.cursor()
            planeta = cursor.execute(SQL, pId).fetchone()
        except sqlite3.Error as error:
            print(error)
        finally:
            self.__conn.close()

        if planeta != None:
            planeta = {'id':planeta[0], 'nome':planeta[1], 'clima':planeta[2],
                       'terreno':planeta[3], 'aparicoes':planeta[4]}

        return planeta


    def removerPlaneta(self, id):
        SQL = "DELETE FROM planeta WHERE id = ?"
        pId = (id,)

        try:
            cursor = self.__conn.cursor()
            result = cursor.execute(SQL, pId).rowcount
            self.__conn.commit()
        except sqlite3.Error as error:
            print(error)
        finally:
            self.__conn.close()

        return result

