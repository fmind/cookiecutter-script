#!/usr/bin/env python3
"""A simple python script."""

import argparse
import logging
import os
import sys

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('infile', type=argparse.FileType('r'))


def f(x):
    """Docstring."""
    return x


if __name__ == '__main__':
    args = PARSER.parse_args()
    sys.tracebacklimit = 0
    logging.basicConfig()

    for line in map(f, args.infile):
        sys.stdout.write(line + os.linesep)
