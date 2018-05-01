number_of_rows = 7

def numberFormat(number):
	if number > 10:
		return " " + str(number) + " "
	else:
		return " " + str(number) + " "

# First Row
row = [1]
print(" " * 7 + numberFormat(row[0]))

# Second Row
row.append(1)
print(" " * 6 + numberFormat(row[0])+ numberFormat(row[1]))

# Third Row
row.append(2)
print(" " * 4 + numberFormat(row[0])+ numberFormat(row[2]) + numberFormat(row[1]))

# Fourth Row
row.append(3)
print(" " * 3 + numberFormat(row[0])+ numberFormat(row[3]) + numberFormat(row[3]) + numberFormat(row[1]))

