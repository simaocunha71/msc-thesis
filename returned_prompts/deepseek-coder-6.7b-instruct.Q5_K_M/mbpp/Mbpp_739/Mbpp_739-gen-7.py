
def find_Index(n):
    index = 1
    while True:
        triangular = index*(index+1)//2
        if len(str(triangular)) == n:
            return index
        index += 1


