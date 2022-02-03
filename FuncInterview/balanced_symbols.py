# -*- coding: utf-8 -*-
"""
Balanced symbols problem code for technical test.
"""
import logging
import sys

sys.path.insert(0, './utils')

from common_utils import checkSymbols, removeComments

def main():
    """
    Main function of Balanced Symbols
    """
    st = input("Please enter a string for check balancing:\n")

    logging.info("Add string for user.")
    logging.info("Remove comments.")
    st = removeComments(st)

    logging.info("Calculate if input is balanced.")
    s_balanced = checkSymbols(st)

    if s_balanced:
        logging.info("String balanced.")
        print("Your string is balanced.")
    else:
        logging.info("String is unbalanced.")
        print("Your string is unbalanced.")

if __name__ == '__main__':
    main()
