def pascal(previous_row):
	next_row = [1]

# working formatting	
	def numberFormat(number):
		if number > 10:
			return " " + str(number) + " "
		else:
			return " " + str(number) + " "
			
	for i in range(len(previous_row)-1):
		next_row.append(previous_row[i] + previous_row[i+1])
	
	next_row.append(1)
	return next_row
	
def test_pascal(start, rows):
	for i in range(rows):
		start = pascal(start)
		print(start)
		
howMany = int(raw_input("How many rows?"))
test_pascal([1,1], howMany)
