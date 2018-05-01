# To see the output, run the following in the Interpreter

# Lambdas ar Function Expressions:
(lambda x, y: x + y)(5, 3)
# returns 8

# In Python the lambda keyword acts a shortcut for declaring small
# anonymous functions:
add = lambda x, y: x + y
add(5, 3)

# check out the output on this one:
print add

# Now in function form:
def add(x, y):
	return x + y
add(5, 3)
# replace return with print to see the output from script mode


# Lambda functions are not bound to a name
# hence, "anonymous"
# They are single-expression functions

# They can't use normal Python statements
# and they always include an implicit "return" statement
