from exp import *

def is_bool(e):
	if(isinstance(e, Type)):
		return e == BoolType
	if(isinstance(e, Expr)):
		return is_bool(check(e))

def is_int(e):
	if(isinstance(e, Type)):
		return e == IntType
	if(isinstance(e, Expr)):
		return is_int(check(e))

def is_same_type(t1, t2):
	if type(t1) != type(t2):
		return False

	if(type(t1) == BoolType or type(t1) == IntType):
		return True

	assert(False)

def expr_same_type(e1, e2):
	return is_same_type(type_check(e1), type_check(e2))

def check_bool(e):
	return BoolType

def check_not(e):
    if(is_bool(e.val)):
    	return BoolType

def check_and(e):
    if(is_bool(e.lhs) and is_bool(e.rhs)):
    	return BoolType

    assert(False)

def check_or(e):
    if(is_bool(e.lhs) and is_bool(e.rhs)):
    	return BoolType

def check_int(e):
	return IntType

def check_if(e):
	pass

def check_math_op(e):
	if(is_int(e.lhs) and is_int(e.rhs)):
		return IntType

	assert False

'''def check_add(e):
	if(is_int(e.lhs) and is_int(e.rhs)):
		return IntType

	assert False

def check_sub(e):
	if(is_int(e.lhs) and is_int(e.rhs)):
		return IntType

	assert False

def check_mult(e):
	if(is_int(e.lhs) and is_int(e.rhs)):
		return IntType

	assert False

def check_div(e):
	if(is_int(e.lhs) and is_int(e.rhs)):
		return IntType

	assert False

def check_mod(e):
	if(is_int(e.lhs) and is_int(e.rhs)):
		return IntType

	assert False

'''

def check_neg(e):
	pass

'''def check_eq(e):
	if(has_same_type(e.lhs, e.rhs)):
		return BoolType

def check_not_eq(e):
	if(has_same_type(e.lhs, e.rhs)):
		return BoolType

def check_gr_than(e):
	if(has_same_type(e.lhs, e.rhs)):
		return BoolType

def check_le_than(e):
	if(has_same_type(e.lhs, e.rhs)):
		return BoolType

def check_gr_than_or_eq(e):
	if(has_same_type(e.lhs, e.rhs)):
		return BoolType

def check_le_than_or_eq(e):
	if(has_same_type(e.lhs, e.rhs)):
		return BoolType'''

def check_boolean_op(e):
	if(has_same_type(e.lhs, e.rhs)):
		return BoolType

def check_id(e):
	return e.ref.type

def check_abs(e):
	t1 = e.var.type_check
	t2 = check(e.expr)
	return ArrowType(t1, t2)

def check_app(e):
	t1 = check(e.lhs)

	if type(t1) is not ArrowType:
		assert False
	if not is_same_type(t1.param, t1):
		assert False

	return t1

def do_check(e):

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

    if type(e) is AddExpr or type(e) is SubExpr or type(e) is MultExpr
    or type(e) is DivExpr or type(e) is ModExpr:
    	return check_math_op(e)

    '''if type(e) is AddExpr:
        return check_add(e)

    if type(e) is SubExpr:
        return check_sub(e)

    if type(e) is MultExpr:
        return check_mult(e)

    if type(e) is DivExpr:
       	return check_div(e)

    if type(e) is ModExpr:
        return check_mod(e)'''

    if type(e) is NegExpr:
        return check_neg(e)

    if type(e) is EqualToExpr or type(e) is NotEqualToExpr or type(e) is GrThanExpr
    or type(e) is GrThanOrEqExpr or type(e) is LethanExpr or type(e) is LeThanOrEqExpr:
    	return check_boolean_op(e)

    '''if type(e) is EqualToExpr:
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
       	return check_le_or_eq(e)'''

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

