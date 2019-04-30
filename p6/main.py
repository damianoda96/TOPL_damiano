import sys
from exp import *
from checking import *
import gen

# Langauge Testing

#e = AndExpr(BoolExpr(True), BoolExpr(True))

# id = AbsExpr(VarDecl("x"), IdExpr("x"))

# t = AbsExpr("a", AbsExpr("b", IdExpr("a")))
# t = AbsExpr("a", AbsExpr("b", IdExpr("b")))

# land = AbsExpr("q", AbsExpr("q", AppExpr(AppExpr(IdExpr("p"), IdExpr("q")), IdExpr("p"))))

# print(land)
# print(id)

# var = VarDecl("a")

# print(var)

#sum0 = math_solve(AddExpr(IntExpr(1), IntExpr(1)))

a = IntExpr(1)
b = IntExpr(1)
c = IntExpr(2)
d = EvalEqualityExpr(EqualToExpr(a,b))
e = EvalEqualityExpr(EqualToExpr(b,c))
f = math_solve(AddExpr(IntExpr(1), IntExpr(1)))

g = GrThanExpr(a,c)

#t = TupleExpr([a, b, c]

int_type = IntType()
bool_type = BoolType()

types = [int_type, bool_type]

uni = UniQuaType(types, TupleType)

print(uni)

# print(EvalMathComparison(g))












