#!/usr/bin/env python3
"""
A simple python script.
"""

import argparse
import logging
import sys

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)


def f(x):
    """Docstring."""
    return x


def {{cookiecutter.script}}(infile):
    text = args.infile.read()

    return f(text)


if __name__ == '__main__':
    args = PARSER.parse_args()
    sys.tracebacklimit = 0
    logging.basicConfig()

    output = {{cookiecutter.script}}(args.infile)
    sys.stdout.write(output)
