# find primes that takes a list of numbers and returns a list conssits of all prime numbrs from the first list
'''
1. Undestand the problems:
	
	understand the relation between data and the solution
	what are we asked to do
	what are we asked to find
	what do we need to show
	what are the inputs that are given 
	what is the output that is expexted
	what are the types of inputs (lists,ints,dictionaries)
	what is the type of output that is expected
	Can you draw a diagram

'''
'''
Devise a plan
#to solve 
#iterate over the numbers in the numbers list.
#check if each number is a prime
#do this by checking if the number i an integer bigger than  1and checking divisibility for all the numbers between 1 and number.
#if the number is prime, add the numebr to out output list
'''
'''
Execute the plan
'''
def find_primes(number_list):
	prime_list = []
	for i in number_list:
		if is_prime(i):
			prime_list.append(i)
	return prime_list
def is_prime(number):
	if(number <= 1) or (number != int(number)):
		return False
	for i in range(2,number):
		if number%i == 0:
			return False
	return True
result = find_primes([-1,0.4,0.2,5,7,9])
print result

'''
Look back , reflect and imrove:


are your sure that the code works as intended?
Is there any way to check the code?
Could you improve the solution in any way?
Will this function be useful for other problems?
'''