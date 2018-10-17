from bottle import get, post, delete, request, response, run
from model.dao.planeta_dao import PlanetaDAO

@post('/planetas')
def adicionarPlaneta():
    dao = PlanetaDAO()
    planeta = (request.json.get('nome'), request.json.get('clima'), request.json.get('terreno'))
    result = dao.adicionarPlaneta(planeta)

    if result > 0:
        response.status = 201
        return {'mensagem':'Planeta adicionado'}
    else:
        response.status = 500
        return {'mensagem':'Erro ao adicionar planeta'}


@get('/')
@get('/planetas')
def listarPlanetas():
    dao = PlanetaDAO()
    planetas = dao.listarPlanetas()
    return planetas


@get('/planetas/<nome>')
def buscarPorNome(nome):
    dao = PlanetaDAO()
    planeta = dao.buscarPorNome(nome)

    if planeta != None:
        return planeta
    else:
        response.status = 404
        return {'mensagem':'Planeta nao encontrado'}


@get('/planetas/id/<id>')
def buscarPorId(id):
    dao = PlanetaDAO()
    planeta = dao.buscarPorId(id)

    if planeta != None:
        return planeta
    else:
        response.status = 404
        return {'mensagem':'Planeta nao encontrado'}


@delete('/planetas/<id>')
def removerPlaneta(id):
    dao = PlanetaDAO()
    result = dao.removerPlaneta(id)

    if result > 0:
        return {'mensagem':'Planeta removido'}
    else:
        response.status = 404
        return {'mensagem':'Planeta nao encontrado'}



if __name__ == '__main__':
    run(host='127.0.0.1', port=8000)

