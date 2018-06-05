#!/usr/bin/env python3
"""Docstring of the program."""

import logging
import argparse

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('input', type=argparse.FileType('r'), help="use '-' for stdin.")


def f(x):
    """Docstring of the function.
    >>> f('hello world')
    'dlrow olleh'"""
    return x[::-1]


def main(args=None):
    opts = parser.parse_args(args)

    for line in opts.input:
        x = line.rstrip()
        print(f(x))


if __name__ == '__main__':
    main()
