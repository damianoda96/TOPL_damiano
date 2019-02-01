import sys
from exp import *
import gen

# -------- BELOW HERE IS ORIGINAL TEST STUFF -----------

e = BoolExpr(True)
e1 = BoolExpr(True)

e2 = BoolExpr(True)
e3 = BoolExpr(True)

e4 = AndExpr(e, e1)
e5 = AndExpr(e2, e3)

# e5 = OrExpr(e, e1)

e7 = AndExpr(e4, e5)

#print(step(e7))

e8 = reduce(e7)

print(e8.val)



# print(e.val)
# print(value(e))
# print(value(e2))
# print(value(e3))
# print(value(e4.expr))
# print(e4.expr.val)

# print(e3.equate().val)



