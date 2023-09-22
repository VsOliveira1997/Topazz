import unittest
from api.api import UserGithub
from helpers.helpers import format_repo,create_file



class TestMain(unittest.TestCase):

    def test_format_repo(self):
        user = UserGithub().get_user('VsOliveira1997')
        repo = UserGithub().get_repo(user)
        self.assertIsNotNone(format_repo(repo))

    def test_create_file(self):
        user = UserGithub().get_user('VsOliveira1997')
        repo = UserGithub().get_repo(user)
        self.assertIsNotNone(create_file(user['name'],repo))

    def test_create_file_error(self):
        self.assertTrue(create_file(1,[]),'Algo deu errado')

    def test_format_repo_error(self):
        self.assertTrue(format_repo([]),'Algo deu errado')


if __name__ == '__main__':
    unittest.main()
