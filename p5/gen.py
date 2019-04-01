import exp
import sl

def gen(e):
    assert isinstance(e, Expr)

    if type(e) is exp.BoolExpr:
        return [sl.Push(e.value)]

    if type(e) is exp.NotExpr:
        return gen(e.expr) + [sl.Not()]

    if type(e) is exp.AndExpr:
        return gen(e.lhs) + gen(e.rhs) + [sl.And()]

    if type(e) is exp.OrExpr:
        return gen(e.lhs) + gen(e.rhs) + [sl.Or()]

    assert False