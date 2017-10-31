"""A generic function used for solving SAT problem."""


def solve(cnf, branch):
    """solve.

    DESCRIPTION: A function used to solve the CNF appling the DPLL
        algorithm (recursive solve) and combining withe the
        chose heuristic function

    INPUTS:
        1.cnf: The CNF formula in the format of Formula Class
        2.heuristc: The chosen heuristc to be applied here
        3.branch: keep track of how many branching has been carried out
            during the search, both successfully and unsucccessfully

            branch[0] = The count of failed branching
            branch[1] = The count of correct branching
    OUtPUT:
        1.cnf: The CNF Formula class that contains a solution in it
    """
    # First, we need to do two preprosessings to speed up the future:
    #   1. Unit Propagation
    #   2. Pure Elimination
    # Both are designed originally in DPLL algorithm

    # Unit Propagation: at each back-tracking level, we need to figure
    #   out how if there any unit-literal clauses we could simplify
    cnf.unitPropagation()

    # Pure Elimination: at each back-tracking leveel, we need to execute
    #   pure elimination to let all clauses contianing them immediately
    #   true in order to speed up the algorithm
    cnf.pureElimination()

    # After these two simplifications, we need to check if there is any
    #   clause becomes empty
    if cnf.has_emptyClause():
        branch[0] += 1
        return False

    # If the CNF has no more clause to apply valuation, then a solution has
    #   been fount. Return immediately
    if cnf.isEmpty():
        return cnf, branch

    # Since the CNF is not empty, nor we have found a failed valuation map, we
    #   need to keep branching, and update the branching counter
    # print("DEBUG: ", len(cnf.clauses))
    heu_literal = cnf.splitting()
    branch[1] += 1
    # print("Chosen: ", heu_literal)
    # First of copying the current CNF for different assignment on chosen literal
    cnfCp = cnf.theForomula()

    # Do two different Assignments
    cnf.assgin(heu_literal, True)
    cnfCp.assgin(heu_literal, False)

    return solve(cnf, branch) or solve(cnfCp, branch)
