from setuptools import setup

setup(
   name='aoc',
   version='1.0',
   description='A handy commandline tool for Advent of Code',
   author='Brent Chesny',
   author_email='brent.chesny@gmail.com',
   packages=['aoc'],
   install_requires=['requests', 'click'],
   entry_points = {
        'console_scripts': ['aoc=aoc.aoc:aoc'],
    }
)
