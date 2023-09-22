from api import UserGithub


def main():
    try:
        get_infos(sys.argv[1])
    except:
        return 'Algo deu errado'


def get_infos(username):
    try:
        return UserGithub().merge_repo_user(username)
    except:
        return 'Problema com o Usuario e/ou Api'



if __name__ == "__main__":
    import sys
    sys.exit(main())
