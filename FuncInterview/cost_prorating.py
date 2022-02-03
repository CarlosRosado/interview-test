# -*- coding: utf-8 -*-
"""
Cost prorating problem code for technical test.
"""
import sys
import logging

sys.path.insert(0, './utils')

from common_utils import costProrating

def main():
    """
    Main function of Cost Prorating
    """
    amount = input("Insert integer for amount:.\n")
    weights = input("Insert list of weights separated by ;...: ")

    logging.info("Amount and weights inserted by user.")
    amount = int(amount)
    weights = [float(x) for x in weights.split(";")]

    logging.info("Calculate the cost prorating.")
    result = costProrating(amount,weights)

    logging.info("Print results.")
    print(result)

if __name__ == '__main__':
    main()
