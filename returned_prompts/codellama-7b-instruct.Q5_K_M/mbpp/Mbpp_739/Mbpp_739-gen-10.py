
def find_Index(n):
    count = 0
    while True:
        count += 1
        triangular = count * (count + 1) // 2
        if len(str(triangular)) == n:
            return triangular


