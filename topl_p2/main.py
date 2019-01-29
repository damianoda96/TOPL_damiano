import sys
from exp import *
import gen
from color import *

def parse(user_input):

	line = user_input.split()

	lib = ["True", "False", "and", "or", "not"]

	for i in line:
		if i not in lib:
			print(i)
			return False
		else:
			continue

	return True


	'''for "True" in line:
		print("True")

	for "False" in line:
		print("False")

	for "AND" in line:
		print("AND")

	for "OR" in line:
		print("OR")

	for "not" in line:
		print("not")'''



# Testing for language functionality

print("__Logic Calculator__\n")

con_color = color()


while(True):

	# take commands 

	user_input = input("::=>> ")

	# parse the line

	if user_input == "quit":
		break
	else:
		if(parse(user_input)):
			print(con_color.OKGREEN + "Good" + con_color.ENDC)
			break
		else:
			print(con_color.FAIL + "Incorrect format..." + con_color.ENDC)
			break

'''e = BoolExpr(True)
e1 = BoolExpr(True)

e2 = AndExpr(e, e1)
e3 = OrExpr(e, e1)
e4 = NotExpr(e)

print(e4)'''

# print(e.val)
# print(value(e))
# print(value(e2))
# print(value(e3))
# print(value(e4.expr))
# print(e4.expr.val)

# print(e3.equate().val)



