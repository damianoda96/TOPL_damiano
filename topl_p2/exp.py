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

class NotExpr(Expr):
    # Represents strings in the form 'not e'
    def __init__(self, e):
        assert isinstance(e, Expr)
        self.expr = e

        if self.expr.val is True:
            self.expr.val = False
        elif self.expr.val is False:
            self.expr.val = True

class BinaryExpr(Expr):
    # Represents form e1 @ e2
    def __init__(self, e1, e2):
        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)
        self.lhs = e1
        self.rhs = e2  # e1

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

    # work on this!!!!!

    def equate(self):
        # print(self.lhs.val)
        # print(self.rhs.val)
        if self.lhs.val or self.rhs.val:
            return BoolExpr(True)
        else:
            return BoolExpr(False)

# -------------- VALUE ----------------------------

def value(e):
    assert isinstance(e, Expr)
    
    if type(e) is BoolExpr:
        return 1
    if type(e) is NotExpr:
        return not value(e.expr)
    
    # if type(e) is isinstance(e, BinaryExpr): #e1 @e2
    # return 1 + max(value(e.lhs) + value(e.rhs))
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
        return 1 + value(e.lhs) + value(e.rhs)

    assert False
