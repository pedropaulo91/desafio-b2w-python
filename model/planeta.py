class Planeta():

    def __init__(self, nome=None, clima=None, terreno=None):
        self.__nome = nome
        self.__clima = clima
        self.__terreno = terreno

    def __init__(self, nome=None, clima=None, terreno=None, aparicoes=None):
        self.__nome = nome
        self.__clima = clima;
        self.__terreno = terreno,
        self.__aparicoes = aparicoes


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def clima(self):
        return self.__clima

    @clima.setter
    def clima(self, clima):
        self.__clima = clima

    @property
    def terreno(self):
        return self.__terreno

    @terreno.setter
    def terreno(self, terreno):
        self.__terreno = terreno

    @property
    def aparicoes(self):
        return self.__aparicoes

    @aparicoes.setter
    def aparicoes(self, aparicoes):
        self.__aparicoes = aparicoes

