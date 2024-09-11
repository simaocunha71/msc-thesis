"""
def count_Primes_nums(n):
    cnt = 0
    for i in range(2,n):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            cnt += 1
    return cnt
"""

