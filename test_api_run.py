import unittest
import requests
from api.api import UserGithub


class TestApiRun(unittest.TestCase):
    response = requests.get('https://api.github.com/users/VsOliveira1997')
    user = UserGithub().get_user('VsOliveira1997')
    repo = UserGithub().get_repo(user)
    merge = UserGithub().merge_repo_user(user)

    def test_request_response(self):
        self.assertTrue(self.response.ok)

    def test_get_user(self):
        self.assertIsNotNone(self.user)

    def test_get_repo(self):
        self.assertIsNotNone(self.repo)

    def test_merge_repo_user(self):
        self.assertIsNotNone(self.merge)

    def test_request_response_error(self):
        response = requests.get('https://api.github.com/users/!!')
        self.assertFalse(response)

    def test_get_user_error(self):
        response = UserGithub().get_user('mshajsndaoquweqweqwe'),
        self.assertEqual( response[0]['message'],'Not Found')

    def test_get_repo_erro(self):
        response = UserGithub().get_repo({'repos_url':'https://api.github.com/users/asjdiojasdiopjsdiopfjiop/repos/sssssssssssssssssssssss'})
        self.assertEqual(response['message'],'Not Found')

    def test_test_merge_repo_user(self):
        response = UserGithub().merge_repo_user('mshajsndaoquweqweqwe')
        self.assertEqual(response, 'Algo deu errado')


if __name__ == '__main__':
    unittest.main()
