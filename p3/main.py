import sys
from exp import *
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

summ = math_step(AddExpr(IntExpr(1), IntExpr(1)))

print(summ)









