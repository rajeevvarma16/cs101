## Program to find all places of occurance of a substring in a given string
danton = "what the hell"*3
print danton
print danton.find("hell")
list = []
list.append(danton.find("hell"))
for i in range(danton.count("hell")-1):
	if(danton.find("hell",list[-1]+1)!= -1):
		print danton.find("hell",list[-1]+1)
		list.append(danton.find("hell",list[-1]+1))
	else:
		break



