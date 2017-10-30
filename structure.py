"""Holding all the structures that are related to a CNF."""
from heuristic import OPTIONS

POSITIVE = True
NEGATE = False


class Var:
    """Var.

    DESCRIPTION: The variable class, that hold all the literals
        (without polarity)
    """

    identifier = 0
    assignment = None

    # Constructing the variable
    def __init__(self, identifier):
        self.identifier = identifier

    # Check if there are two variables the same by comparing identifiers
    def __eq__(self, new_var):
        return self.identifier == new_var.identifier

    # Since the variables hare are immutable, and we would like
    #   to use hash for dictionary, hasing by its ID
    def __hash__(self):
        return hash(self.identifier)

    # Class method
    def assign(self, v):
        self.assignment = v


class Literal:
    """Literal.

    DESCRIPTION: The literals class, similar to the variables, but it contains polarity
    """

    var_name = None
    polarity = POSITIVE

    # Constructing this literal
    def __init__(self, id, polarity):
        self.var_name = id
        self.polarity = polarity

    # Hashing by the sum of it's polarity and variable ID
    def __hash__(self):
        return hash(self.polarity) + hash(self.var_name)

    # Check if the given new literal is actually the same variable
    #   as the current one but only with opposite polarity
    def opp_var(self, new_l):
        return (self.var_name == new_l.var_name) and \
               (self.polarity != new_l.polarity)

    # Get the value assigned to a literal
    def get_val(self):
        if self.var_name.assignment is None:
            return None
        else:
            return (not self.polarity) ^ self.var_name.assignment

    # Assign value to a literal by assigning the value to its varibale
    def assign(self, v):
        self.var_name.assign((not self.polarity) ^ v)

    # Assign a literal with None for re-using it
    def redo_assgin(self):
        self.var_name.assign(None)


class Clause:
    """Clause.

    DESCRIPTION: A clase for all the sigle clauses that consist
        up the whole CNF
    """

    # A list to hold all the literals in this clause
    all_literals = []

    def __init__(self, all_literals):
        self.all_literals = all_literals

    # A method to check if the current clause is actually empty
    # This information is helpful since empty clause makes the
    #   whole CNF to be False
    def isEmpty(self):
        if len(self.all_literals) == 0:
            return True
        else:
            return False

    # A method to detect if the current clause is actually a
    #   unit cluase, so we could apply Unit Propagation
    def isUnit(self):
        if len(self.all_literals) == 1:
            return self.all_literals[0]
        else:
            return False


class Formula:
    """Formula.

    DESCRIPTION: A class for all the conjunctive normal form
        formulas that we acuqire in reading the puzzle.

    FIELDS:
        1. clauses: the biggest element of a CNF fomula
        2. unit_Clause: all the unit clauses for Unit Propagation
        3. pure_Literals: all the literals for Pure Elimination
        4. solution: a list of string that keep track of the solution to
            this formula
        5. heuristicsFcn: the heuristics function that will be
            applied here
    """

    clauses = []
    unit_Clause = []
    pure_Literals = []
    solution = []
    heuristicsFcn = ""

    def __init__(self, clauses, unit_Clause, pure_Literals, solution, heuristicsFcn):
        self.clauses = clauses
        self.unit_Clause = unit_Clause
        self.pure_Literals = pure_Literals
        self.solution = solution
        self.heuristicsFcn = heuristicsFcn

    # Aquire all the literals showed up in the formula
    def get_all_literals(self):
        all_literals = []
        for clause in self.clauses:
            for literal in clause.all_literals:
                all_literals.append(literal)
        return all_literals

    # Check if there is no clause contianed in this formula anymroe
    def isEmpty(self):
        if len(self.clauses) == 0:
            return True
        else:
            return False

    # Check if there is any empty claue for immediate decision
    def has_emptyClause(self):
        for clause in self.clauses:
            if len(clause.all_literals) == 0:
                return True
        return False

    # Get the solution
    def get_solution(self):
        result = sorted(self.solution, key=lambda i: abs(int(i)))
    return result

    # Applying the current valuation and get simplified
    #   version of the formula
    # Clauses with one or more than one True literals will
    #   be true, so it will be deleted
    # Clauses that has literals are False should have all
    #   of them deleted
    def simplify(self):
        self.clauses = filter(
            lambda clause: len(filter(
                lambda literal: literal.value(),  clause.all_literals)) == 0, self.clauses)

        for clause in self.clauses:
            clause.all_literals = filter(
                lambda literal: literal.value() is not False,
                clause.all_literals)

    # Apply value assginment to the literal in the CNF
    def assgin(self, literal, val):
        if value:
            # put this assignement on the list firt as a string
            self.solution.append(str(literal))
        literal.assign(val)
        # simplify the CNF immediately after this assignment
        self.simplify()
        literal.redo_assgin()

    # Using heuristic function to choose a literal to split
    #   the entire CNF
    def splitting(self):
        return OPTIONS[self.heuristic](self)
