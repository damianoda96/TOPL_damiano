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

#sum0 = math_step(AddExpr(IntExpr(1), IntExpr(1)))

a = IntExpr(1)
b = IntExpr(1)
c = IntExpr(2)
x = EvalEqualityExpr(EqualToExpr(a,b))
y = EvalEqualityExpr(EqualToExpr(b,c))

print(x)
print(y)








