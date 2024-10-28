"""
def amicable_numbers_sum(n):
    return sum(
        i for i in range(1, n+1)
            if sum(d for d in range(1, int(i**0.5)+1) if i%d == 0) == i
                and sum(d for d in range(1, int(i**0.5)+1) if i%d == 0) == i
    )
"""
