# import sys

# Expression Language for Theory of Programming Language
#
# Following along with Dr. Sutton's lectures and implementation
# 

class Expr:

    # --- Boolean stuff --

    # e ::= true
    #   false
    #   not e1
    #   e1 and e2
    #   e1 or e2

    #v ::= true
    #      false

    # --- lambda stuff ---

    # e::= x
    #      x.e1
    #      e1 e2

    pass

# Bool Stuff ------------------------------------


class BoolExpr(Expr):

    # True and False

    def __init__(self, val):

        assert (val == True or val == False)
        self.val = val

    def __str__(self):

    	if self.val == True:
            return "True"
        else:
            return "False"

    def equate(self):
        return self.val


class NotExpr(Expr):

    # not e

    def __init__(self, e):
        assert isinstance(e, Expr)
        self.expr = e

    def __str__(self):
    	return ("not ( " + str(e.expr) + " )")

    def equate(self):

        return not e


class AndExpr(Expr):

    # e1 and e2

    def __init__(self, e1, e2):

        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)

        self.lhs = e1
        self.rhs = e2

    def __str__(self):
    	return (str(self.lhs) + " and " + str(self.rhs))


class OrExpr(Expr):

    # e1 or e2

    def __init__(self, e1, e2):

        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)

        self.lhs = e1
        self.rhs = e2

    def __str__(self):

    	return (str(self.lhs) + " or " + str(self.rhs))


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

# ------------- SAME --------------------

def same(e, e1):

    assert isinstance(e, Expr)
    assert isinstance(e1, Expr)

    if type(e) == type(e1):

        if(height(e) == height(e1)):

            e = reduce(e)
            e1 = reduce(e1)

            if e.val == e1.val:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# ------------- STEPS for BOOL --------------------

def step_not(e):

    if is_value(e):

        if e.val:
            return BoolExpr(False)
        else:
            return BoolExpr(True)

    else:

        return NotExpr(step(e.expr))


def step_and(e):

    # e and e1

    if is_value(e.lhs) and is_value(e.rhs):

        if e.lhs.val and e.rhs.val:
            return BoolExpr(True)
        else:
            return BoolExpr(False)

    if is_reducible(e.lhs):
        return AndExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return AndExpr(e.lhs, step(e.rhs))

    assert False

def step_or(e):

    if is_value(e.lhs) and is_value(e.rhs):

        if e.lhs.val or e.rhs.val:
            return BoolExpr(True)
        else:
            return BoolExpr(False)

    if is_reducible(e.lhs):
        return OrExpr(step(e.lhs), e.rhs)

    if is_reducible(e.rhs):
        return OrExpr(e.lhs, step(e.rhs))

    assert False


def step(e):

    if(is_reducible(e)):

        assert isinstance(e, Expr)

        if type(e) is BoolExpr:
            return e

        if type(e) is NotExpr:
            return step_not(e.expr)

        if type(e) is AndExpr:
            return step_and(e)

        if type(e) is OrExpr:
            return step_or(e)


# ----------------- REDUCE -------------------

def reduce(e):

    while(is_reducible(e)):

        e = step(e)

    return e

# ---- BOOL Helpers

def is_value(e):

    if(type(e) == BoolExpr):
        return True
    else:
        return False

def is_reducible(e):

    if(is_value(e)):
        return False
    else:
        return True


# ---------------------- LAMBA STUFF ------------------++++

class IdExpr(Expr):

  	# Identifiers

  	def __init__(self, id):
  		self.id = id
  		self.ref = None

  	def __str__(self):
  		return self.id

class VarDecl(Expr):

  	# Declaration of a variable

  	def __init__(self, id):
  		self.id = id

  	def __str__(self):
  		return self.id


class AbsExpr(Expr):

  	# Lambda Expressiones

  	def __init__(self, var, e1):

  		if type(var) is str:
  		    self.var = VarDecl(var)
  		else:
  			self.var = var
  		self.expr = e1

  	def __str__(self):
  		return f"\\{self.var}.{self.expr}"

class MultiAbsExpr(Expr): 

	# for multi argument abstractions

	def __init__(self, var, e1, e2):

  		if type(var) is str:
  		    self.var = VarDecl(var)
  		else:
  			self.var = var
  		self.expr1 = e1
  		self.expr2 = e2

  	def __str__(self):
  		return f"\\{self.var}.{self.expr1}{self.expr2}"


class AppExpr(Expr):

	# Application

  	def __init__(self, lhs, rhs):

  		self.lhs = lhs
  		self.rhs = rhs

  	def __str__(self):
  		return f"({self.lhs} {self.rhs})"

 class CallDecl(Expr):

 	# For Function Declarations 

 	def __init__(self, id, params):
 		self.id = id
 		self.param_types = param_types

 	def __str__(self):
  		return self.id

 class CallFunct(Expr):

 	# For function call expressions

 	def __init__(self, id, params):
 		self.id = id
 		self.params = params


 	def __str__(self):
  		return self.id

def lam_is_value(e):

    return type(e) in (IdExpr, AbsExpr)

def lam_is_reducible(e):

    return not is_value(e)

def resolve(e, scope = []): # for name resolution

    if type(e) is AppExpr:
        resolve(e.lhs, scope)
        resolve(e.rhs, scope)
        return

    if type(e) is AbsExpr:
        resolve(e.expr, scope + [e.var])
        return

    if type(e) is IdExpr:
        for var in reversed(scope):
            if e.id == var.id:
                e.ref = var
                return

        raise Exception("name lookup error")

    assert False

def lam_subst(e, s):

	if type(e) is IdExpr:
		if e.ref in s: 
			return s[e.ref]
		else:
			return e

	if type(e) is AbsExpr:
		return AbsExpr(e.var, lam_subst(e.expr, s))

	if type(e) is AppExpr:
		return AppExpr(lam_subst(e.lhs, s), lam_subst(e.rhs), s)

	assert(False)


def step_app(e):

 	if lam_is_reducible(e.lhs):
 		return AppExpr(step(e.lhs), e.rhs)

 	if type(e.lhs) is not AbsExpr:
 		raise Exception("Application of non-Lambda")

 	if lam_is_reducible(e.rhs):
 		return AppExpr(e.lhs, step(e.rhs))

 	s = {e.lhs.var: e.rhs}

 	return subst(e.lhs.expr, s)

def step_lam(e):

  	assert isinstance(e, Expr)
  	assert lam_is_reducible(e)

  	if type(e) is AppExpr:
  		step_app(e)

  	assert False


