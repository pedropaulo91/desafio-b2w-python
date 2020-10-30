from bottle import get, post, delete, request, response, run
from model.dao.planeta_dao import PlanetaDAO

@post('/api/planetas')
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



@get('/api/planetas')
def listarPlanetas():
    dao = PlanetaDAO()
    planetas = dao.listarPlanetas()
    return planetas


@get('/api/planetas/nome/<nome>')
def buscarPorNome(nome):
    dao = PlanetaDAO()
    planeta = dao.buscarPorNome(nome)

    if planeta != None:
        return planeta
    else:
        response.status = 404
        return {'mensagem':'Planeta nao encontrado'}


@get('/api/planetas/id/<id>')
def buscarPorId(id):
    dao = PlanetaDAO()
    planeta = dao.buscarPorId(id)

    if planeta != None:
        return planeta
    else:
        response.status = 404
        return {'mensagem':'Planeta nao encontrado'}


@delete('/api/planetas/<id>')
def removerPlaneta(id):
    dao = PlanetaDAO()
    result = dao.removerPlaneta(id)

    if result > 0:
        return {'mensagem':'Planeta removido'}
    else:
        response.status = 404
        return {'mensagem':'Planeta nao encontrado'}



if __name__ == '__main__':
    run(host='localhost', port=8000)

