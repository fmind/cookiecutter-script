#!/usr/bin/env python3
"""
A simple python script.
"""

import argparse
import sys

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
PARSER.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)


def f(x):
    """Function doc."""
    return x


def main(args):
    text = args.infile.read()

    return f(text)


if __name__ == '__main__':
    args = PARSER.parse_args()
    args.outfile.write(main(args))
