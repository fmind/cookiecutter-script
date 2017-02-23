#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple python script.
"""

from __future__ import print_function

import argparse
import sys

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
PARSER.add_argument('outfile', nargs='?', type=argparse.FileType('w'), default=sys.stdout)


def f(x):
    """Function doc."""
    return x


def main(args):
    x = args.infile.read()

    return f(x)


if __name__ == '__main__':
    try:
        args = PARSER.parse_args()
        args.outfile.write(main(args))
        sys.exit(0)
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)
