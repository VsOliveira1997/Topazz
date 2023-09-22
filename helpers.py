import json
import os
def format_repo(repo_obj):
    try:
        new_repo = {
            'name': [],
            'fullname': []
        }
        for x in range(len(repo_obj)):
            new_repo['name'].append(repo_obj[x].get('full_name'))
            new_repo['fullname'].append(repo_obj[x].get('name'))
        return new_repo
    except:
        return 'Algo deu errado'

def create_file(name, json):
    try:
        with open(os.path.join('Usuarios',name+'.txt'), 'w') as f:
            f.write(json)
    except:
        return 'Algo deu errado'


