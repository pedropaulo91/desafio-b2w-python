import unittest
from unittest import TestCase
from unittest.mock import patch

@patch('model.dao.planeta_dao.PlanetaDAO')
class PlanetaDAOTests(TestCase):

    def test_adicionarPlaneta(self, PlanetaDAO):
        dao = PlanetaDAO()
        dao.adicionarPlaneta.return_value = 1
        planeta = ('Novo planeta', 'Novo clima', 'Novo clima')
        self.assertGreater(dao.adicionarPlaneta(planeta), 0)

    def test_adicionarPlanetas(self, PlanetaDAO):
        dao = PlanetaDAO()
        dao.adicionarPlanetas.return_value = 61
        planetas = []
        self.assertEqual(61, dao.adicionarPlanetas(planetas))


    def test_listarPlanetas(self, PlanetaDAO):
        dao = PlanetaDAO()
        dao.listarPlanetas.return_value = dict
        self.assertEqual(dict, dao.listarPlanetas())


    def test_buscarPorNome(self, PlanetaDAO):
        dao = PlanetaDAO()
        dao.buscarPorNome.return_value = dict
        self.assertEqual(dict, dao.buscarPorNome('Tatooine'))


    def test_buscarPorId(self, PlanetaDAO):
        dao = PlanetaDAO()
        dao.buscarPorId.return_value = dict
        self.assertEqual(dict, dao.buscarPorId(1))


    def test_removerPlaneta(self, PlanetaDAO):
        dao = PlanetaDAO()
        dao.removerPlaneta.return_value = 1
        self.assertGreater(dao.removerPlaneta(1), 0)


if __name__ == "__main__":
    unittest.main()