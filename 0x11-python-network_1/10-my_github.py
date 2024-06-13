#!/usr/bin/python3
"""Request id from GitHub API
"""

import requests
from sys import argv

def main(argv):
    """
    Script that takes your GitHub credentials (username and password) and
    uses the GitHub API to display your id.
    """
    user = argv[1]
    password = argv[2]
    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(user, password))
    try:
        profile_info = response.json()
        print(profile_info['id'])
    except:
        print('None')

if __name__ == "__main__":
    main(argv)
