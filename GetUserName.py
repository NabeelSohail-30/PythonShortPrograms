import getpass


def get_username():
    username = getpass.getuser()
    print("user name: " + username)

get_username()