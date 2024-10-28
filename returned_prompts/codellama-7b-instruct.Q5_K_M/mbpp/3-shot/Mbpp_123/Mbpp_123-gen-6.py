
def amicable_numbers_sum(num: int) -> int:
    sum = 0
    for i in range(1, num+1):
        if sum(set(list(str(i)))) == i:
            sum += i
    return sum


