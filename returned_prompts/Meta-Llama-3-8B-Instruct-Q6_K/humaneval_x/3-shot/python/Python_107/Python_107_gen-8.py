    even_count = 0
    odd_count = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    return (even_count, odd_count)
    # or return tuple(map(lambda x: sum(1 for i in range(1, n+1) if str(i) == str(i)[::-1] and i % x == 0), (0, 1)))  # one liner solution

