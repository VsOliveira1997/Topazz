import unittest
import requests
from api import UserGithub


class TestApiRun(unittest.TestCase):

    def test_request_response(self):
        response = requests.get('https://api.github.com/users/VsOliveira1997')
        self.assertTrue(response.ok)

    def test_get_user(self):
        response = UserGithub().get_user('VsOliveira1997')
        self.assertIsNotNone(response)

    def test_get_repo(self):
        user = UserGithub().get_user('VsOliveira1997')
        response = UserGithub().get_repo(user)
        self.assertIsNotNone(response)

    def test_merge_repo_user(self):
        user = UserGithub().get_user('VsOliveira1997')
        response = UserGithub().merge_repo_user(user)
        self.assertIsNotNone(response)

    # Error part

    def test_request_response_error(self):
        response = requests.get('https://api.github.com/users/!!')
        self.assertFalse(response)

    def test_get_user_error(self):
        response = UserGithub().get_user('!!')
        self.assertEquals(response['message'],'Not Found')

    def test_get_repo_erro(self):
        response = UserGithub().get_repo({'repos_url':'# https://api.github.com/users/!!/repos'})
        self.assertEquals(response['message'],'Not Found')

    def test_request_response_error(self):
        user = UserGithub().get_user('!!!')
        response = UserGithub().merge_repo_user(user)
        self.assertEquals(response,'Algo deu errado')


if __name__ == '__main__':
    unittest.main()
