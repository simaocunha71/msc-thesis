
def bell_number(n):
    bell = [0]*(n+1)
    bell[0] = 1
    bell[1] = 2
    for i in range(2,n+1):
        for j in range(i):
            bell[i] += bell[j] * bell[i-1-j]
    return bell[n]


