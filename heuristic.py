"""Heuristic functions in this file."""

from collections import defaultdict
import random
import math


# random heuristic
def random_heuristic(cnf):
    return random.choice(cnf.get_literals())


# helper function counting occurance of literal
def occurance_counter(clauses):
    # score of each variables
    # a dictionary object
    score = defaultdict(lambda: [0, 0])

    # a set if returned literals and its score
    ref = {}
    added = {}

    incrementor = 1

    for clause in clauses:
        for literal in clause.all_literals:
            if literal.polarity:
                i = 0
            else:
                i = 1
            score[literal.var_name][i] += incrementor

            ref[(literal.var_name, literal.polarity)] = literal

    added = {key: value[0] + value[1] for key, value in score.iteritems()}

    # get max occurance
    m = max(added, key=added.get)

    # check polarity
    if score[m][0] >= score[m][1]:
        polarity = True
    else:
        polarity = False

    return ref[(m, polarity)]


# get the clauses with minimum Size
def min_size_clause(clauses):

    s = -1
    min_clauses = []

    for clause in clauses:
        size = len(clauses.all_literals)
        # add equal or smaller size of clause
        if size < s or s == -1:
            min_clauses = [clause]
            s = size
        elif s == size:
            min_clauses.append(clause)

    return min_clauses


# Freeman's POSIT Maximum Occurance in clauses of Minimum Size
def POSIT(cnf):
    # get clauses with minimum size
    min_clauses = min_size_clause(cnf.clauses)
    return occurance_counter(min_clauses)


# global variables of heuristics option
options = {"random": random_heuristic, "POSIT": POSIT}
