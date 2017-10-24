def stamps(n):
    five_p = n/5
    rem = n%5
    two_p = rem/2
    one_p = rem%2
    return five_p,two_p,one_p
    
    # Your code here


print stamps(8)