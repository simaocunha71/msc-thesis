
def d(n):
    s = 1
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s += i
            if i*i != n:
                s += n//i
    return s

def amicable_numbers_sum(n):
    res = 0
    for i in range(1, n+1):
        if i < d(i) and d(d(i)) == i:
            res += i
    return res


