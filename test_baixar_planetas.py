import unittest
from unittest import TestCase
from unittest.mock import patch

class BaixarPlanetasTests(TestCase):

    @patch('baixar_planetas.getQtdPlanetas', return_value = 61)
    def test_getQtdPlanetas(self, getQtdPlanetas):
        self.assertEqual(getQtdPlanetas(), 61)


    @patch('baixar_planetas.main', return_value = True)
    def test_main(self, main):
        self.assertTrue(main())

if __name__ == "__main__":
    unittest.main()