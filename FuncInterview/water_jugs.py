# -*- coding: utf-8 -*-
"""
Water Jugs problem code for technical test.
"""
import sys
import logging

sys.path.insert(0, './utils')

from juggers_utils import Jugger,JuggersGraph

def main():
    """
	Main function of Water Juggs
	"""
    jugs = input("Insert Jug sizes, separated by ;...:.\n")
    target = input("Insert target: ")
    logging.info("juggs and target inserted by user.")

    jugs = [Jugger(int(x)) for x in jugs.split(";")]
    target = int(target)

    logging.info("Calculate Jugger Graph.")
    plt = JuggersGraph(jugs, target)
    plt.grapher()

    logging.info("Print the Jugger solution problem.")
    plt.print_graph_solutions()

if __name__ == '__main__':
    main()
