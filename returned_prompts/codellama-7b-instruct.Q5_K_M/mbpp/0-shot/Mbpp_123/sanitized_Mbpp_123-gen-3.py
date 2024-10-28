def amicable_numbers_sum(n):
    return sum(x for x in range(1,n+1) if sum(d for d in range(1,x+1) if x%d==0)==x and sum(d for d in range(1,x+1) if x%d==0)==x)