
    even = 0
    odd = 0

    num = abs(num)

    while num > 0:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
        num = num // 10

    return (even, odd)


print(even_odd_count(-12))  # ==> (1, 1)
print(even_odd_count(123))  # ==> (1, 2)

This code works by iterating through each digit in the integer, and checking if it is even or odd. If it is even, the even counter is incremented by 1, if it is odd, the odd counter is incremented by 1. Finally, the counters are returned in a tuple.

The absolute value is used to handle negative numbers by making them positive for the iteration.
"""

# 2.
"""
