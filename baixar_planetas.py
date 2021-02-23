"""
Módulo para obter os planetas da API
e inserir no banco de dados.
"""
import requests, json
from model.planeta import Planeta
from model.dao.planeta_dao import PlanetaDAO

planetas = []

def getQtdPlanetas():
    response = requests.get('https://swapi.dev/api/planets')
    content = json.loads(response.content)
    qtdPlanetas = int(content['count'])
    return qtdPlanetas


def main():
    for i in range(1, getQtdPlanetas()+1):

        response = requests.get('https://swapi.dev/api/planets/{}'.format(i))
        dictPlaneta = json.loads(response.content)

        planeta = Planeta()

        planeta.nome = dictPlaneta['name']
        planeta.clima = dictPlaneta['climate']
        planeta.terreno = dictPlaneta['terrain']
        planeta.aparicoes = len(dictPlaneta['films'])

        planetas.append((planeta.nome, planeta.clima, planeta.terreno, planeta.aparicoes))

    dao = PlanetaDAO()
    dao.adicionarPlanetas(planetas)


if __name__ == "__main__":
    main()

