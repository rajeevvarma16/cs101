def union(a,b):
	for elem in a:
		if elem in b:
			b = b.remove(elem)
	print a + b
	#a = list(set(a).union(set(b)))
	#return a
a = union([2,3,4],[4,5,5])
print a