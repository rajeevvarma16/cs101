def even_average(list):
	even_numbers = []
	for i in list:
		if is_even(i):
			even_numbers.append(i)
	average = sum(even_numbers)/len(even_numbers)
	print even_numbers
	return average
def is_even(number):
	if (number <0) and (n != int(number)):
		return False
	if number%2!=0:
		return False
	return True
result = even_average([1,2,3,5234,8,5,4,6])
print result