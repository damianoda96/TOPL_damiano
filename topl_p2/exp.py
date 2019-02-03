# import sys

# Expression Language (EL)

class Expr:

    # e ::= true
    #   false
    #   not e1
    #   e1 and e2
    #   e1 or e2

    pass

class BoolExpr(Expr):
    # Represents the strings True and False
    def __init__(self, val):
        assert (val is True or val is False)
        self.val = val

    def equate(self):
        return self.val

class NotExpr(Expr):
    # Represents strings in the form 'not e'
    def __init__(self, e):
        assert isinstance(e, Expr)
        self.expr = e

        '''if self.expr.val is True:
            self.expr.val = False
            self.val = False
        elif self.expr.val is False:
            self.expr.val = True
            self.val = False'''

    def equate(self):
        return not e
        #return not self.expr.val

'''class BinaryExpr(Expr):
    # Represents form e1 @ e2
    def __init__(self, e1, e2):
        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)
        self.lhs = e1
        self.rhs = e2  # e1'''

class AndExpr(Expr):
    # Represents string in the form 'e1 and e2'
    def __init__(self, e1, e2):
        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)
        self.lhs = e1
        self.rhs = e2

    def equate(self):
        return self.lhs and self.rhs


class OrExpr(Expr):
    # Represents string in the form 'e1 or e2'
    def __init__(self, e1, e2):
        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)
        self.lhs = e1
        self.rhs = e2

    def equate(self):
        return self.lhs and self.rhs

# -------------- VALUE ----------------------------

def value(e):
    assert isinstance(e, Expr)
    
    if type(e) is BoolExpr:
        return 1
    if type(e) is NotExpr:
        return not value(e.expr)

    if type(e) is AndExpr:
        return value(e.lhs) and value(e.rhs)
    
    if type(e) is OrExpr:
        return value(e.lhs) or value(e.rhs)

    assert False

# ------------ SIZE -------------------------------

def size(e):
    assert isinstance(e, Expr)

    if type(e) is BoolExpr:
        return 1

    if type(e) is NotExpr:
        return 1 + size(e.expr)

    if type(e) is AndExpr:
        return 1 + size(e.lhs) + size(e.rhs)

    if type(e) is OrExpr:
        return 1 + size(e.lhs) + size(e.rhs)

    assert False

# ------------ HEIGHT ---------------------

def height(e):
    assert isinstance(e, Expr)

    if e is None:
        return 0

    if type(e) is BoolExpr:
        return 1

    if type(e) is NotExpr:
        return 1 + height(e.expr)

    if type(e) is AndExpr or type(e) is OrExpr:

        left_height = height(e.lhs)
        right_height = height(e.rhs)

        if left_height > right_height:
            return (left_height + 1)
        else:
            return (right_height + 1)

    '''if type(e) is OrExpr:

        left_height = height(e.lhs)
        right_height = height(e.rhs)

        if left_height > right_height:
            return (left_height + 1)
        else:
            return (right_height + 1)'''

# ------------- SAME --------------------

def same(e, e1):
    assert isinstance(e, Expr)
    assert isinstance(e1, Expr)

    if type(e) == type(e1):

        e = reduce(e)
        e1 = reduce(e1)

        if e.val == e1.val:
            return True
        else:
            return False

    else:

        return False

# ------------- STEP --------------------

def step(e):
    assert isinstance(e, Expr)
    # returns an expression after 1 step through e

    if type(e) is BoolExpr:
        return e

    if type(e) is NotExpr:
        return not e

    if type(e) is AndExpr:
        return e.equate()

    if type(e) is OrExpr:
        return e.equate()


# ----------------- REDUCE -------------------

def reduce(e):
    assert isinstance(e, Expr)

    if type(e) is BoolExpr:
        return e

    if type(e) is NotExpr:
        return reduce(not e)

    if type(e) is AndExpr:
        return reduce(e.equate())

    if type(e) is OrExpr:
        return reduce(e.equate())

