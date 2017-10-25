def symmetric(p):
    n = len(p)
    i = 0
    if n == 0:
        return True
    if n == 1 and len(p[0])==1:
        return True
    if n == 1 and len(p[0])!=1:
        return False
    if n > 1:
        while i < n:
            j = 0
            while j < n:
                if p[i][j] != p[j][i]:
                    return False
                j = j+ 1
            i = i + 1
        return True
    else:
        return False
    
    # Your code here

print symmetric([[1, 2, 3],
                [2, 5, 4],
                [3, 4, 1]])