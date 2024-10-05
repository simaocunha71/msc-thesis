
def count_up_to(n):
    if n < 2:
        return []
    if n == 2:
        return [2]

    prime_numbers = [2, 3]
    i = 5
    while i < n:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)
        i += 4
    return prime_numbers


# Test cases
assert(count_up_to(5) == [2, 3])
assert(count_up_to(11) == [2, 3, 5, 7])
assert(count_up_to(0) == [])
assert(count_up_to(20) == [2, 3, 5, 7, 11, 13, 17, 19])
assert(count_up_to(1) == [])
assert(count_up_to(18) == [2, 3, 5, 7, 11, 13, 17])


print('All test cases passed.')



















































































































































































































