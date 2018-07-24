#!/usr/bin/env python3
"""Documentation of the program."""

import logging
import argparse

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('input', type=argparse.FileType('r'), help="- for stdin.")


def reverse(x):
    """Documentation of the function.
    >>> reverse('hello world !')
    '! dlrow olleh'"""
    return x[::-1]


def main(args=None):
    opts = parser.parse_args(args)

    for line in opts.input:
        print(reverse(line.rstrip()))


if __name__ == '__main__':
    main()
