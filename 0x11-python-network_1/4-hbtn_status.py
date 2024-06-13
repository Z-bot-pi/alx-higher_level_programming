#!/usr/bin/python3
"""Fetch url https://alx-intranet.hbtn.io/status using requests module
"""

import requests


def main():
    """
    Function that fetches https://intranet.hbtn.io/status
    """
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url)
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))

if __name__ == "__main__":
    main()
