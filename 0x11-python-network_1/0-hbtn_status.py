#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        ctnt = resp.read()
        utf8_ctnt = ctnt.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(ctnt)))
        print("\t- content: {}".format(ctnt))
        print("\t- utf8 content: {}".format(utf8_ctnt))
