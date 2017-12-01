#!/usr/bin/env python3
"""A simple python script."""

import argparse
import logging
import sys

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument('files', type=argparse.FileType('r'))


def f(x):
    """Docstring."""
    return x


def main(args):
    logging.basicConfig()
    opts = PARSER.parse_args(args)

    for file in opts.files:
        print(f(file))


if __name__ == '__main__':
    main(sys.argv[1:])
