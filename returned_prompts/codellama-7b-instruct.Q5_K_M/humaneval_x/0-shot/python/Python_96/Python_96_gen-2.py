
def count_up_to(n):
    if n < 1:
        return []
    prime_numbers = []
    for i in range(2, n + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
    return prime_numbers
