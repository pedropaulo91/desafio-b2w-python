import unittest
from unittest import TestCase
from unittest.mock import patch

class AppTests(TestCase):

    @patch('app.adicionarPlaneta', return_value = dict)
    def test_adicionarPlaneta(self, adicionarPlaneta):
        self.assertEqual(adicionarPlaneta(), dict)

    @patch('app.listarPlanetas', return_value=dict)
    def test_listarPlanetas(self, listarPlanetas):
        self.assertEqual(listarPlanetas(), dict)

    @patch('app.buscarPorNome', return_value=dict)
    def test_buscarPorNome(self, buscarPorNome):
        self.assertEqual(buscarPorNome('Tatooine'), dict)

    @patch('app.buscarPorId', return_value=dict)
    def test_buscarPorId(self, buscarPorId):
        self.assertEqual(buscarPorId(1), dict)

    @patch('app.removerPlaneta', return_value=dict)
    def test_removerPlaneta(self, removerPlaneta):
        self.assertEqual(removerPlaneta(1), dict)


if __name__ == "__main__":
    unittest.main()