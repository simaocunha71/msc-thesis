def second_smallest(numbers):
    m1, m2 = float('inf'), float('inf')
    for n in numbers:
        if n <= m1:
            m1, m2 = n, m1
        elif n < m2:
            m2 = n
    return m2