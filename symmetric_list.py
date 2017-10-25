def symmetric(p):
    n = len(p)
    i = 0
    while i < n:
        j = 0
        while j < n:
            print p[i][j]
            print p[j][i]
            if p[i][j] != p[j][i]:
                return False
            j = j+ 1
        i = i + 1
    return True
    
    # Your code here

print symmetric([[1, 2, 3],
                [2, 5, 4],
                [3, 4, 1]])