from exp import *

def check_bool(e):
	pass

def check_not(e):
    pass

def check_and(e):
    pass

def check_or(e):
    pass

def check_int(e):
	pass

def check_if(e):
	pass

def check_add(e):
	pass

def check_sub(e):
	pass

def check_mult(e):
	pass

def check_div(e):
	pass

def check_mod(e):
	pass

def check_neg(e):
	pass

def check_eq(e):
	pass

def check_not_eq(e):
	pass

def check_gr_than(e):
	pass

def check_le_than(e):
	pass

def check_gr_than_or_eq(e):
	pass

def check_le_than_or_eq(e):
	pass

def check_id(e):
	pass

def check_abs(e):
	pass

def check_app(e):
	pass

def do_check(e):

    # implement all of this stuff

    assert isinstance(e, Expr)

    if type(e) is BoolExpr:
        return check_bool(e)

    if type(e) is NotExpr:
        return check_not(e)

    if type(e) is AndExpr:
        return check_and(e)

    if type(e) is OrExpr:
        return check_or(e)

    if type(e) is IntExpr:
       	return check_int(e)

    if type(e) is IfExpr:
        return check_if(e)

    if type(e) is AddExpr:
        return check_add(e)

    if type(e) is SubExpr:
        return check_sub(e)

    if type(e) is MultExpr:
        return check_mult(e)

    if type(e) is DivExpr:
       	return check_div(e)

    if type(e) is ModExpr:
        return check_mod(e)

    if type(e) is NegExpr:
        return check_neg(e)

    if type(e) is EqualToExpr:
        return check_eq(e)

    if type(e) is NotEqualToExpr:
        return check_not_eq(e)

    if type(e) is GrThanExpr:
        return check_gr_than(e)

    if type(e) is LethanExpr:
        return check_le_than(e)

    if type(e) is GrThanOrEqExpr:
        return check_gr_or_eq(e)

    if type(e) is LeThanOrEqExpr:
       	return check_le_or_eq(e)

    if type(e) is IdExpr:
        return check_id(e)

    if type(e) is AbsExpr:
        return abs_expr(e)

    if type(e) is AppExpr:
       	return check_app(e)

def type_check(e):

    if not e.type:
        e.type = do_check(e)

    return e.type

