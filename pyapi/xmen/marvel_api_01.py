import argparse
import time
import hashlib

import requests

XAVIER = 'http://gateway.marvel.com/v1/public/characters'

def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup):
    url = XAVIER + "?name=" + lookmeup + "&ts=" + stampystamp + "&apikey=" + pkeyz + "&hash=" + hashyhash
    r = requests.get(url)

    print(url)

    return r.json()


def main():
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')

    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')

    nightcrawler = str(time.time()).rstrip('.')

    cerebro = hashbuilder(nightcrawler, beast, storm)

    uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, "Wolverine")

    print(uncannyxmen)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    args = parser.parse_args()
    main()
