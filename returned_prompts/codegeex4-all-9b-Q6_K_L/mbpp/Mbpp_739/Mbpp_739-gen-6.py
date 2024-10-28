def find_Index(n):
    m=1
    while True:
        if len(str(m*(m+1)//2))==n:
            return m
        m+=1

