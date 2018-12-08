import click
from datetime import date
import os
import requests

AOC_SESSION_COOKIE_FILE = '~/.aoc_session'

def get_aoc_session_path():
    return os.path.expanduser(AOC_SESSION_COOKIE_FILE)

def get_latest_aoc_year():
    return date.today().year

def load_session_cookie():
    if not os.path.isfile(get_aoc_session_path()):
        return None

    with open(get_aoc_session_path()) as file:
        session_cookie = file.read()
    return session_cookie

@click.group()
def aoc():
    pass

@aoc.command()
@click.argument('session_cookie')
def set_session(session_cookie):
    with open(get_aoc_session_path(), 'w+') as file:
        file.write(session_cookie)

@aoc.command()
def get_session():
    print(load_session_cookie())

@aoc.command()
@click.argument('day')
@click.option('--year', '-y', default=get_latest_aoc_year(), help='The AoC year you want to get the input for')
@click.option('--output', '-o', help='The file output filename')
def input(day, year, output):
    session_cookie = load_session_cookie()
    if not session_cookie:
        print('No session cookie set. Use the following command to set up your session cookie: aoc set-session [SESSION_COOKIE]')
        return

    url = 'https://adventofcode.com/{}/day/{}/input'.format(year, day)
    headers = {'Cookie': 'session={}'.format(session_cookie)}
    r = requests.get(url, headers=headers)

    if not output:
        output = 'day-{:02}.txt'.format(int(day))

    with open(output, 'w+') as file:
        file.write(r.text)
