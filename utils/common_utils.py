"""
Common utilities
"""
import re
import math

def checkSymbols(symbolString):
    """
    Function for check balanced symbols
    :param symbolString: string for checking balanced symbols
    :return: True if string is balanced or False if is unbalanced
    """
    open_symbols = tuple('({[')
    close_symbols = tuple(')}]')
    map_symbols = dict(zip(open_symbols, close_symbols))
    st = []

    for i in symbolString:
        if i in open_symbols:
            st.append(map_symbols[i])
        elif i in close_symbols:
            if not st or i != st.pop():
                return False
    if not st:
        return True
    else:
        return False

def replacer(match):
    """
    Function for replacer character
    :param match: string for replacing
    :return: string replaced
    """
    str = match.group(0)
    if str[0] == '/': 
        return ""
    return str

def removeComments(symbolString):
    """
    Function for remove /**/ comments
    :param symbolString: string to remove characters
    :return: string without comment characters
    """
    comments_regex = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL)
    return comments_regex.sub(replacer, symbolString) 

def costProrating(amount, weights):
    """
    Function for calculate cost of Prorating
    :param amount: amount 
    :param weights: list of weights
    :return: List of prorating costs
    """
    totalWeight = sum(weights)
    length = len(weights)

    actual = []
    error = []
    rounded = []

    added = 0
    i = 0

    for w in weights:
        actual.insert(i,amount * (w / totalWeight))
        rounded.insert(i,math.floor(actual[i]))
        error.insert(i,actual[i] - rounded[i])
        added += rounded[i]
        i += 1

    while added < amount:
        maxError = 0.0
        maxErrorIndex = -1
        for e in range(length):
            if error[e] > maxError:
                maxError = error[e]
                maxErrorIndex = e

        rounded[maxErrorIndex] += 1
        error[maxErrorIndex] -= 1

        added += 1
    return rounded
