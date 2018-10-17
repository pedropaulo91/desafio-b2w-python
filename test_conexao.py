import unittest
from unittest import TestCase
from model.dao import conexao

class TestConexao(TestCase):

	def test_conectar(self):
		self.assertIsNotNone(conexao.conectar())


if __name__ == "__main__":
	unittest.main()