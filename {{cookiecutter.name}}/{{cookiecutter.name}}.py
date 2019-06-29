#!/usr/bin/env python3

"""Documentation of the script."""

import argparse
import logging

logging.basicConfig(level=logging.INFO)

PARSER = argparse.ArgumentParser(description=__doc__)
PARSER.add_argument("input", type=argparse.FileType("r"))


def reverse(s: str) -> str:
    """Documentation of the function.

    >>> reverse('hello world !')
    '! dlrow olleh'"""
    return s[::-1]


def main(args=None):
    opts = PARSER.parse_args(args)

    print(reverse(opts.input.read()))


if __name__ == "__main__":
    main()
