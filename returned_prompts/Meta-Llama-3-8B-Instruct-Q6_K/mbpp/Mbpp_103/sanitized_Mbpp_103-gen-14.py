import math
def eulerian_num(n, m):
    result = 0
    for i in range(m+1):
        result += (-1)**i * math.comb(n, i)
    return result