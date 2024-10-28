def divisor_sum(n):
    div_sum = 1
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            if i * (n // i) == n:
                div_sum = div_sum + i + n//i
            else:
                div_sum = div_sum + i
            i += 1
    return div_sum
def amicable_numbers_sum(limit):
    result = 0
    arr = [0] * (limit+1)
    for i in range(1, limit+1):
        arr[i] = divisor_sum(i)
    for i in range(1, limit+1):
        if arr[i] != i and arr[i] <= limit and arr[arr[i]] == i:
            result += i
    return result