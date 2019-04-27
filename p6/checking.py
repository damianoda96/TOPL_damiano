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

def is_same_type(t1 : Type, t2 : Type):
	if type(t1) != type(t2):
		return False

	if(type(t1) == BoolType or type(t1) == IntType):
		return True

	assert(False)

# ---- Universally Quanitified Types -----

def is_tuple(t : Type):
    return type(t) is TupleExpr

def is_record(t : Type):
    return type(t) is RecordExpr

def is_variant(t : Type):
    return type(t) is VariantExpr

# ---------

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

def check_if(e : Expr):
	pass

def check_math_op(e : Expr):
	if(is_int(e.lhs) and is_int(e.rhs)):
		return IntType

	assert False

def check_neg(e : Expr):
	pass

def check_boolean_op(e : Expr):
	if(has_same_type(e.lhs, e.rhs)):
		return BoolType

def check_id(e : Expr):
	return e.ref.type

def check_abs(e : Expr):
	t1 = e.var.type_check
	t2 = check(e.expr)
	return ArrowType(t1, t2)

def check_app(e : Expr):
	t1 = check(e.lhs)

	if type(t1) is not ArrowType:
		assert False
	if not is_same_type(t1.param, t1):
		assert False

	return t1

def check_tuple(e : Expr):
	pass

def check_record(e : Expr):
	pass

def check_variant(e : Expr):
	pass

def do_check(e : Expr):

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

    if (type(e) is AddExpr or type(e) is SubExpr or type(e) is MultExpr
    or type(e) is DivExpr or type(e) is ModExpr):
    	return check_math_op(e)

    if type(e) is NegExpr:
        return check_neg(e)

    if (type(e) is EqualToExpr or type(e) is NotEqualToExpr or type(e) is GrThanExpr
    or type(e) is GrThanOrEqExpr or type(e) is LethanExpr or type(e) is LeThanOrEqExpr):
    	return check_boolean_op(e)

    if type(e) is IdExpr:
        return check_id(e)

    if type(e) is AbsExpr:
        return check_abs(e)

    if type(e) is AppExpr:
       	return check_app(e)

    if type(e) is TupleExpr:
    	return check_tuple(e)

    if type(e) is RecordExpr:
    	return check_record(e)

    if type(e) is VariantExpr:
    	return check_variant(e)

    assert(False)

def type_check(e : Expr):

    if not e.type:
        e.type = do_check(e)

    return e.type

