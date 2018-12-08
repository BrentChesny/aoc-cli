# Advent of Code: CLI

This simple command-line tool can be used to quickly fetch the input data for Advent of Code.

## Installation

```console
$ git clone https://github.com/BrentChesny/aoc-cli.git
$ cd aoc-cli
$ python setup.py install
```

## Usage

First you need to set your session cookie for Advent of Code. To get this session cookie, log in on adventofcode.com and grab the content of the `session` cookie using your favorite browser.

```console
$ aoc set-session <session-cookie>
```

Next, you can use the tool as follows to fetch your personal puzzle input:

```console
$ aoc input 9
```

Where `9` is the day you want to get input for. Optionally you can specify an output filename using the `-o` or `--output` flag. The tool will default to the current Advent of Code year. You can use the `-y` or `--year` flag to set a specific year.

```console
$ aoc input 9 --year 2016 --output input.txt
```
