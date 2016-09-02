#!/usr/bin/python3

import argparse
import sys
import unittest

"""
Calculate interest.
"""

def interest(type, principal, rate, duration):
    """Get amount due (including principal) with given interest rate and time.
    """
    if type is "simple":
        return principal * (1 + duration * rate)
    elif type is "compound":
        return principal * (1 + rate) ** duration

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Calculate interest accrued.')
    parser.add_argument('--type', required=True, help="'simple' | 'compound'")
    parser.add_argument('--principal', required=True, help='starting amount')
    parser.add_argument('--rate', required=True, help='interest rate in [0, 1]')
    parser.add_argument('--duration', required=True, help='number of times interest updated')
    args = parser.parse_args(sys.argv[1:])
    print(interest(vars(args)['type'], vars(args)['principal'], \
          vars(args)['rate'], vars(args)['duration']))
