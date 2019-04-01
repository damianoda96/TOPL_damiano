# JVM like assembly language for propositional calculus (basic logic)
#
# A program consists of a series of instructions
#
# Instructions:
#
# i ::= push true
#      push false
#      pop
#      and
#      or
#      not
#
# A value is: True or False

import exp

class Instr:
    pass
class Push(Instr):
    def __init__(self, val):
        self.value = val

    def __str__(self):
        return f"push {self.value}"

class Pop(Instr):
    pass

class And(Instr):
    pass

class Or(Instr):
    pass

class Not(Instr):
    def __str__(self):
        return "not"

# ------------------------- RUN ----------------------

def run(prog):
    stack = []
    for ip in range(len(prog)):

        insn = prog[ip]

        if type(insn) is Push:
            print(f"{prog[ip:]} x {stack}")
            stack.append(insn.value)

        if type(insn) is Pop:
            print(f"{prog[ip:]} x {stack}")
            stack.pop()

        if type(insn) is And:
            print("And")
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 and v2)

        if type(insn) is Or:
            print("Or")
            v1 = stack.pop()
            v2 = stack.pop()
            stack.append(v1 or v2)

        if type(insn) is Not:
            print("Not")
            v1 = stack.pop()
            stack.append(not v1)

    return stack[-1]


# --------------------- EXPR -------------------------


def expr(prog):
    stack = []
    for insn in prog:
        if type(insn) is Push:
            stack.append(exp.BoolExpr(insn.value))

        if type(insn) is Pop:
            stack.pop()

        if type(insn) is And:

            e1 = stack.pop()
            e2 = stack.pop()
            stack.append(exp.AndExpr(e1, e2))

        if type(insn) is Or:

            e1 = stack.pop()
            e2 = stack.pop()
            stack.append(exp.OrExpr(e1, e2))

        if type(insn) is Not:
            v1 = stack.pop()
            stack.append(exp.NotExpr(v1))

