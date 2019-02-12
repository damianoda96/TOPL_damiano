# import sys

# Expression Language (EL)

class Expr:

    # e ::= true
    #   false
    #   not e1
    #   e1 and e2
    #   e1 or e2

    #v ::= true
    #      false

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

    #def equate(self):
        #return self.lhs and self.rhs


class OrExpr(Expr):
    # Represents string in the form 'e1 or e2'
    def __init__(self, e1, e2):
        assert isinstance(e1, Expr)
        assert isinstance(e2, Expr)
        self.lhs = e1
        self.rhs = e2

    def equate(self):
        return self.lhs and self.rhs


# ---------------------- NEW STUFF ------------------++++

class IdExpr(Expr):
  	'''Represents identifiers'''
  	def __init__(self, id):
  		self.id = id

  	def __str__(self):
  		return self.id

class VarDecl(Expr):
  	'''Represents the declaration of a variable'''
  	def __init__(self, id):
  		self.id = id


class AbsExpr(Expr):
  	'''Represents lambda abstractions'''

  	def __init__(self, id, e1):
  		self.id = id
  		self.expr = e1

  	def __str__(self):
  		return f"\\{self.id}.{self.expr}"

class AppExpr(Expr):

  	def __init__(self, lhs, rhs):
  		self.lhs = lhs
  		self.rhs = rhs

  	def __str__(self):
  		return f"({self.lhs} {self.rhs})"


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

# ------------- STEP --------------------

def step_not(e):

	if is_value(e):
		if e.val:
			return BoolExpr(False)
		else:
			return BoolExpr(True)

	if type(e) is NotExpr:
		return not e.expr

	if type(e) is AndExpr:

		if isreducible(e.lhs) and isreducible(e.rhs):

			return not (e.lhs and e.rhs)

		elif isreducible(e.lhs) and not is_reducible(e.rhs):

			return not (e.lhs and e.rhs)

	elif type(e) is OrExpr:

		return not e.lhs or e.rhs

	assert False


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
        # returns an expression after 1 step through e

        if type(e) is BoolExpr:
            return e

        if type(e) is NotExpr:
            '''
            not true -> false
             not false -> true
            '''
            '''if is_value(e.expr):
                if e.expr.val == True:
                    return BoolExpr(False)
                else:
                    return BoolExpr(True)

            return not step(e.expr)'''

            return step_not(e.expr)

        if type(e) is AndExpr:
            return step_and(e)

        if type(e) is OrExpr:
            return step_or(e)


# ----------------- REDUCE -------------------

def reduce(e):
    '''#assert(is_reducible(e))
    assert isinstance(e, Expr)

    if type(e) is BoolExpr:
        return e

    if type(e) is NotExpr:
        return reduce(not e)

    if type(e) is AndExpr:
       return reduce(e.equate())

    if type(e) is OrExpr:
        return reduce(e.equate())'''

    while(is_reducible(e)):
        e = step(e)

    return e

def is_value(e):
    # returns true if e is irriducible
    return type(e) is BoolExpr

def is_reducible(e):
    return not is_value(e)


