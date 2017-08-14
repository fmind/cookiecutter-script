#!/usr/bin/env python3
"""A simple python script."""

import argparse
import logging

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('infile', type=argparse.FileType('r'))


def f(x):
    """Docstring."""
    return x


if __name__ == '__main__':
    args = PARSER.parse_args()
    logging.basicConfig()

    for line in args.infile:
        print(f(line))
