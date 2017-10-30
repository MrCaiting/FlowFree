"""Read clauses and setup structures."""

import structure


def get_variables(cnf):
    """get_variables.

    DESCRIPTION: get unique variables in CNF.
    """
    variables = []
    for i in range(len(cnf)):
        for j in cnf[i]:
            if abs(j) in variables:
                continue
            else:
                variables.append(abs(j))
    return sorted(variables)


def get_literals(cnf):
    """get_literals.

    DESCRIPTION: for convenience getting every element in the cnf
    """
    return [j for i in cnf for j in i]


def convert(clauses, option):
    """convert.

    DESCRIPTION: setup structures

    """
    # get unique variables
    variables = {i: structure.Var(i) for i in get_variables(clauses)}

    # get literals
    literals = {i: structure.Literal(variables[abs(i)], (
        i >= 0)) for i in set(get_literals(clauses))}

    # set clauses
    clauses = structure.Clause(clauses)

    print("Input number of clauses to the solver: %s" % len(clauses))
    print("Input number of variables to the solver: %s" % len(variables))
    print("Input number of literals to the solver: %s" % len(literals))

    return structure.Formula(clauses, [], option, [], [])
