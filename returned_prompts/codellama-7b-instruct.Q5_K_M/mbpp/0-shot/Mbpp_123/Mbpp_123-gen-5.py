def amicable_numbers_sum(max_n):
    amicable_numbers = []
    for i in range(1, max_n+1):
        if i in amicable_numbers:
            continue
        d1 = sum(j for j in range(1, i//2+1) if i%j==0)
        d2 = sum(j for j in range(1, d1//2+1) if d1%j==0)
        if d1==i and d2==i:
            amicable_numbers.append(i)
    return sum(amicable_numbers)
