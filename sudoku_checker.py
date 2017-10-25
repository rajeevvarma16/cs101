'''
checks if the input sudoku is a valid one or not
'''
def check_sudoku(p):
	n = len(p)
	digit = 1
	while digit <=n:# Go through each digit 
		i = 0
		while i < n:# Go through each row and column
			row_count = 0
			col_count = 0
			j = 0
			while j<n:# for each entry in ith row 
				if p[i][j] == digit:
					row_count +=1
				if p[j][i] == digit:
					col_count +=1
				j = j + 1
			if row_count != 1 or col_count != 1:
				return False
			i = i + 1
		digit = digit + 1
	return True

print check_sudoku([[1,2,3],[3,1,2],[2,3,1]])

