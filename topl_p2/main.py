import sys
from exp import *
import gen

# -------- BELOW HERE IS ORIGINAL TEST STUFF -----------

'''e = BoolExpr(False)
e1 = BoolExpr(True)

e3 = NotExpr(e1)

andexp = AndExpr(e, e1)

e4 = NotExpr(andexp)

e2 = BoolExpr(True)
e3 = BoolExpr(False)

e4 = AndExpr(e, e1)
e5 = AndExpr(e2, e3)

e6 = OrExpr(e, e1)
e7 = OrExpr(e2, e3)

e8 = AndExpr(e4, e5)
e9 = AndExpr(e6, e7)

e10 = OrExpr(e6, e7)

# print(reduce(e6).val)
# print(reduce(e10).val)

# print(height(e10))

print(reduce(e4).val)'''

id = AbsExpr(VarDecl("x"), IdExpr("x"))

e1 = AppExpr(id, IdExpr("y"))

print(id)
print(e1)








