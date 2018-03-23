# Challenge: Fill your basket with 20 tomatoes
# Replace the ?? with the correct number

# BONUS: 
	# WHAT statement can you add to check how many tomatoes we have?
	# WHERE can you correctly put this statement?

basketFull = False
tomatoes = 0
while not basketFull:
	tomatoes += 1
	if tomatoes > 19:
		print tomatoes
		# More descriptive output:
		print("I have " + str(tomatoes) + " tomatoes in my basket!")
		basketFull = True
