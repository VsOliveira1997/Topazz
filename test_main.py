import unittest
from main import main,get_infos



class TestMain(unittest.TestCase):

    def test_main_function_erro(self):
        self.assertTrue(main(),'Algo deu errado')

    def test_get_infos_erro(self):
        self.assertTrue(get_infos(''), 'Problema com o Usuario e/ou Api')

    def test_get_infos(self):
        self.assertIsNotNone(get_infos('VsOliveira1997'))


if __name__ == '__main__':
    unittest.main()
