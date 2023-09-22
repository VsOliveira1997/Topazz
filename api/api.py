# https://api.github.com/users/USERNAME/repos
# https://api.github.com/users/VsOliveira1997

import json
import requests
from helpers.helpers import  format_repo,create_file
class UserGithub:
    def __init__(self) -> None:
        self.url = 'https://api.github.com/users/'
    def get_user(self, user):
        try:
            user = requests.get(url=self.url+user)
            return user.json()
        except:
            return 'Algo deu errado'

    def get_repo(self, user):
        try:
            repos = requests.get(url=user['repos_url'])
            return repos.json()
        except:
            return 'Algo deu errado'

    def merge_repo_user(self,username):
        try:
            rep_user = self.get_user(username)
            rep_repos = self.get_repo(rep_user)

            return_data = json.dumps({
                'nome': rep_user['name'],
                'perfil': rep_user['login'],
                'rep_publico': rep_user['public_repos'],
                'seguidores': rep_user['followers'],
                'seguindo': rep_user['following'],
                "repos": format_repo(rep_repos)

            }, indent=2)

            create_file(rep_user['login'],return_data)
            return return_data
        except:
            return 'Algo deu errado'



