# import sys

# Expression Language for Theory of Programming Language
#
# Following along with Dr. Sutton's lectures and implementation
# 

class Type:

    # T ::= Bool
    #		Int
    #		T1 -> T2	Abstraction types
    #		(T1, T2, ... , Tn) -> T0	Lambda types

    pass

class BoolType(Type):

    def __str__(self):
    	return "Bool"

class IntType(Type):

    def __str__(self):
    	return "Int"

class ArrowType(Type):

	def __init__(self, t1, t2):
		self.param = t1
		self.ret = t2

	def __str__(self):
		return str(self.param) + " -> " + str(self.ret)

class FnType(Type):

    # Type Int

    def __init__(self, params, ret):
    	self.params = params
    	self.ret = ret

    def __str__(self):
    	return "Function"

class Expr:

    # --- Boolean stuff --

    # e ::= true
    #   false
    #   not e1
    #   e1 and e2
    #   e1 or e2

    # v ::= true
    #      false

    # --- lambda stuff ---

    # e::= x
    #      x.e1
    #      e1 e2

    # Implement math expressions

    # e ::  e1 + e2
    #       e1 - e2
    #       e1 * e2
    #       e1 / e2

    def __init__(self, Expr):
        # type of the expression 
        self.type = None
        self.Expr = Expr
        self.type = do_check(Expr)

    def __str__(self):
        return self.Expr

    pass

# Tuples

class TupleExpr(Expr):
	def __init__(self, items):
		self.items = items
		self.size = len(items)

	def __str__(self):
		return (self.items)

# Records

class RecordExpr(Expr):
	pass

# Variants

class VariantExpr(Expr):
	pass

# Conditional Exprs

class IfExpr(Expr):

	def __init__(self, e1, e2, e3):
		self.conditional = e1
		self.true = e2
		self.false = e3

	def __str__(self):
		return ("if " + str(self.conditional) + " then " + str(self.true) + " else " + str(self.false))

# Bool Stuff ------------------------------------


class BoolExpr(Expr):

    # True and False

    def __init__(self, val):

        assert (val == True or val == False)
        self.val = val
        self.type = "BoolExpr"

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
        self.type = "NotExpr"

    def __str__(self):
    	return ("not ( " + str(self.expr) + " )")

    def equate(self):
        return not e


class AndExpr(Expr):

    # e1 and e2

    def __init__(self, e1, e2):

        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)

        self.lhs = e1
        self.rhs = e2
        self.type = "AndExpr"

    def __str__(self):
    	return (str(self.lhs) + " and " + str(self.rhs))


class OrExpr(Expr):

    # e1 or e2

    def __init__(self, e1, e2):

        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)

        self.lhs = e1
        self.rhs = e2
        self.type = "OrExpr"

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

# ---------- COMPARISON EXPR'S ----------

class GrThanExpr(Expr): # e1 > e2

    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return (str(self.lhs) + " > " + str(self.rhs))

class LethanExpr(Expr): # e1 < e2
    
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return (str(self.lhs) + " < " + str(self.rhs))

class GrThanOrEqExpr(Expr): # e1 >= e2
    
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return (str(self.lhs) + " >= " + str(self.rhs))

class LeThanOrEqExpr(Expr): # e1 <= e2
    
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return (str(self.lhs) + " <= " + str(self.rhs))

def EvalMathComparison(e): # evaluating comparisons

	types =[IntExpr, AddExpr, SubExpr, MultExpr, DivExpr]

	assert(e.lhs and e.rhs) # assert we have a left amd right operands
	assert(type(e.lhs) in types) # make sure is math type
	assert(type(e.rhs) in types)

	lhs = math_solve(e.lhs)
	rhs = math_solve(e.rhs)

	if type(e) is GrThanExpr:
		if is_gr(lhs, rhs):
			return BoolExpr(True)
		else:
			return BoolExpr(False)
	elif type(e) is GrThanOrEqExpr:
		if is_gr_or_eq(lhs, rhs):
			return BoolExpr(True)
		else:
			return BoolExpr(False)
	elif type(e) is LethanExpr:
		if is_le(lhs, rhs):
			return BoolExpr(True)
		else:
			return BoolExpr(False)
	elif type(e) is LeThanOrEqExpr:
		if is_le_or_eq(lhs, rhs):
			return BoolExpr(True)
		else:
			return BoolExpr(False)
	else:
		assert(False)

# Helpers

def is_gr(lhs, rhs):
	return lhs.val > rhs.val
def is_le(lhs, rhs):
	return lhs.val < rhs.val
def is_gr_or_eq(lhs, rhs):
	return lhs.val >= rhs.val
def is_le_or_eq(lhs, rhs):
	return lhs.val <= rhs.val



# ------ For both Bool and Int exprs -------

class EqualToExpr(Expr): # e1 == e2
    
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return (str(self.lhs) + " == " + str(self.rhs))

class NotEqualToExpr(Expr): # e1 != e2
    
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2

    def __str__(self):
        return (str(self.lhs) + " != " + str(self.rhs))

def EvalEqualityExpr(e):

	math_types = ["IntExpr", "AddExpr", "SubExpr", "MultExpr", "DivExpr"]
	bool_types = ["BoolExpr", "NotExpr", "AndExpr", "OrExpr"]

	which_eval = ""

	assert(e.lhs and e.rhs)

	if(e.lhs.type in math_types): # right and left sides must be same type, bool or int
		assert(e.rhs.type in math_types)
		which_eval = "math"
	if(e.lhs.type in bool_types):
		assert(e.rhs.type in bool_types)
		which_eval = "bool"

	if type(e) == EqualToExpr:
		if which_eval == "math":
			if check_equality(math_solve(e.lhs), math_solve(e.rhs)):
				return(BoolExpr(True))
			else:
				return(BoolExpr(False))
		else:
			if check_equality(reduce(e.lhs), reduce(e.rhs)):
				return(BoolExpr(True))
			else:
				return(BoolExpr(False))

	if type(e) == NotEqualToExpr:
		if which_eval == "math":

			if check_equality(math_solve(e.lhs), math_solve(e.rhs)):
				return(BoolExpr(False))
			else:
				return(BoolExpr(True))
		else:
			if check_equality(reduce(e.lhs), reduce(e.rhs)):
				return(BoolExpr(False))
			else:
				return(BoolExpr(True))
	
	assert(False)

def check_equality(lhs, rhs):
	return lhs.val == rhs.val



# ---------- MATH EXPR'S ----------------

class IntExpr(Expr):

    def __init__(self, val):
        assert(type(val) == int)
        self.val = val
        self.type = "IntExpr"
    
    def __str__(self):
        return str(self.val)

class AddExpr(Expr): # e1 + e2

    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2
        self.type = "AddExpr"

    def __str__(self):
        return (str(self.lhs) + " + " + str(self.rhs))

class SubExpr(Expr): # e1 - e2
    
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2
        self.type = "SubExpr"

    def __str__(self):
        return (str(self.lhs) + " - " + str(self.rhs))

class MultExpr(Expr): # e1 * e2
    
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2
        self.type = "MultExpr"

    def __str__(self):
        return (str(self.lhs) + " * " + str(self.rhs))

class DivExpr(Expr): # e1 / e2
    
    def __init__(self, e1, e2):
        self.lhs = e1
        self.rhs = e2
        self.type = "DivExpr"

    def __str__(self):
        return (str(self.lhs) + " / " + str(self.rhs))

# MATH TODO, Make these work with our step function:

class ModExpr(Expr): # e1 % e2

	def __init__(self, e1, e2):
		self.lhs = e1
		self.rhs = e2
		self.type = "ModExpr"

	def __str__(self):
		return (str(self.lhs) + " % " + str(self.rhs))

class NegExpr(Expr):

	def __init__(self, e1):
		self.expr = e1

	def __str__(self):
		return ("-" + str(expr))



# ------- MATH EVALUATION -----

def math_step_add(e):
    
    if e.lhs.type == "IntExpr" and e.rhs.type == "IntExpr":
        return IntExpr(e.lhs.val + e.rhs.val)

    if math_is_reducible(e.lhs):
        return AddExpr(math_solve(e.lhs), e.rhs)

    if math_is_reducible(e.rhs):
        return AddExpr(e.lhs, math_solve(e.rhs))

    assert False

def math_step_sub(e):

    if e.lhs.type == "IntExpr" and e.rhs.type == "IntExpr":
        return IntExpr(e.lhs.val - e.rhs.val)

    if math_is_reducible(e.lhs):
        return SubExpr(math_solve(e.lhs), e.rhs)

    if math_is_reducible(e.rhs):
        return SubExpr(e.lhs, math_solve(e.rhs))

    assert False

def math_step_mult(e):

    if e.lhs.type == "IntExpr" and e.rhs.type == "IntExpr":
        return IntExpr(e.lhs.val * e.rhs.val)

    if math_is_reducible(e.lhs):
        return MultExpr(math_solve(e.lhs), e.rhs)

    if math_is_reducible(e.rhs):
        return MultExpr(e.lhs, math_solve(e.rhs))

    assert False

def math_step_div(e):

    if e.lhs.type == "IntExpr" and e.rhs.type == "IntExpr":
        return IntExpr(int(e.lhs.val / e.rhs.val))

    if math_is_reducible(e.lhs):
        return DivExpr(math_solve(e.lhs), e.rhs)

    if math_is_reducible(e.rhs):
        return DivExpr(e.lhs, math_solve(e.rhs))

    assert False

def math_step_mod(e):

    if e.lhs.type == "IntExpr" and e.rhs.type == "IntExpr":
        return IntExpr(e.lhs.val % e.rhs.val)

    if math_is_reducible(e.lhs):
        return ModExpr(math_solve(e.lhs), e.rhs)

    if math_is_reducible(e.rhs):
        return ModExpr(e.lhs, math_solve(e.rhs))

    assert False

def math_step_neg(e):

	if e.type == "IntExpr":
		return (IntExpr(e.val * -1))

	if math_is_reducible(e):
		return NegExpr(math_solve(e))

def math_solve(e):
    
    if(math_is_reducible(e)):

        if type(e) == IntType:
            return e

        if type(e) == AddExpr:
            return math_step_add(e)

        if type(e) == SubExpr:
            return math_step_sub(e)

        if type(e) == MultExpr:
            return math_step_mult(e)

        if type(e) == DivExpr:
            return math_step_div(e)

        if type(e) == ModExpr:
        	return math_step_mod(e)

        if type(e) == NegExpr:
        	return math_step_neg(e)

        raise Exception("Type of math exp is invalid")

    else:
    	return e
    

def math_is_reducible(e):

    # if e is not a raw integer value
    
    if(math_is_value(e)):
        return False
    else:
        return True

def math_is_value(e):

    if(type(e) == IntExpr):
        return True
    else:
        return False


# ---------------------- LAMBA EXPR'S ------------------++++

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

  	def __init__(self, var, e):

  		if type(var) is str:
  		    self.var = VarDecl(var)
  		else:
  			self.var = var

  		self.expr = e

  	def __str__(self):
  		return (str(self.var) + './' + str(self.expr))

class MultiAbsExpr(Expr): 

	# for multi argument abstractions

    def __init__(self, var, args):

        if type(var) is str:
            self.var = VarDecl(var)
        else:
            self.var = var

        # list of aguments

        self.args = args

    def __str__(self):

        return (str(self.val) + args)


class AppExpr(Expr):

	# Application

  	def __init__(self, lhs, rhs):

  		self.lhs = lhs
  		self.rhs = rhs

  	def __str__(self):

  		return ('( ' + str(self.lhs) + ' , ' + str(self.rhs) + ' )')

class CallDecl(Expr):

 	# For Function Declarations 

 	def __init__(self, id, params):

 		self.id = id
 		self.params = params

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

    if(type(e) == IdExpr or type(e) == AbsExpr):
        return True
    else:
        return False

def lam_is_reducible(e):

    return not lam_is_value(e)

def resolve(e, scope = []): 

    # for name resolution

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

    if lam_is_reducible(e.rhs):
        return AppExpr(e.lhs, step(e.rhs))

    if type(e.lhs) is not AbsExpr:
        raise Exception("Non Lambda Application")

    s = {e.lhs.var: e.rhs}

    return lam_subst(e.lhs.expr, s)

def step_lam(e):
  	assert isinstance(e, Expr)
  	assert lam_is_reducible(e)

  	if type(e) is AppExpr:
  		step_app(e)

  	assert False


