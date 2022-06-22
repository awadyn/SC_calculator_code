########################
# PL: Python
# PL translator: python3 interpreter
# To translate and run this Python script:	python3 calculate.py
#
########################
# write your code below:
########################

# defining global variables




# NOTE: define any global variables that you need here
# e.g. x1
x1 = 0
# TODO: any others you need to define?




# global variables have been defined...
#######################################
# defining calculator functions




# NOTE: define a function that 1) requires 2 parameter inputs, 2) calls them x & y,
#	3) computes their sum, and 4) returns their sum to the 'caller' function
def add(x, y):
	# TODO write function code here



# TODO: repeat for subtract() ...
# def subtract(...):
#	...
#	...

# TODO: repeat for multiply() ...

# TODO: repeat for divide() ...




# calculator functions have been defined...
###########################################
# defining program logic functions




# NOTE: define a function to get inputs from user and save them to variables
# 	such that the other calculator functions can use them
# NOTE: this function does not return anything in particular
# we need 3 inputs: x1 and x2 (integers) and an operator (character)
def get_input():
	# declare any global variables used in this function
	# e.g. x1
	global x1		

	print("Enter x1: ")
	input1 = input()
	# NOTE: the data type of input1 is a string, we must use a
	# casting operation to change its type from string to integer
	# --> Python integer casting operation is a function, called int()
	x1 = int(input1)
	print("Enter operator: ")

	# TODO: complete this function...



###############################
	# Python if/else syntax
	# if (condition):
	# 	# code goes here
	# else:
	# 	#code goes here
# NOTE: define a function that uses an if/else conditional
#	to decide what calculator function to call according to
#	the user's input operator
#	--> this function should then call the correct
#	    calculator function
# NOTE: this function does not return anything in particular
def calculate():
	if (operator == '+'):
		# TODO: complete this conditional
	# TODO: complete this function
	#	(no need to use else, but you can)




# all functions have been defined...
###########################################




# NOTE: a main function similar to the one in C
def main():
	get_input()
	calculate()
	print(result)

# NOTE: now tell the python interpreter to run main()
main()





