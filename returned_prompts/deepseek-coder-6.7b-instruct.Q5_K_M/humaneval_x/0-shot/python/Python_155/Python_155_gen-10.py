
    def even_odd_count(num):
        even_count = 0
        odd_count = 0
        for digit in str(abs(num)):
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        return (even_count, odd_count)

    print(even_odd_count(-12))  # ==> (1, 1)
    print(even_odd_count(123))  # ==> (1, 2)



"""

def even_odd_count(num):
    even_count = 0
    odd_count = 0
    for digit in str(abs(num)):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return (even_count, odd_count)

print(even_odd_count(-12))  # ==> (1, 1)
print(even_odd_count(123))  # ==> (1, 2)
"""

# Test Cases:

assert even_odd_count(-12) == (1, 1)
assert even_odd_count(123) == (1, 2)
assert even_odd_count(456) == (3, 0)
assert even_odd_count(0) == (1, 0)
assert even_odd_count(7895643210) == (5, 3)
print('All test cases pass')

# Sample Tests:

# print(even_odd_count(-12))  # ==> (1, 1)
# print(even_odd_count(123))  # ==> (1, 2)
# print(even_odd_count(456))  # ==> (3, 0)
# print(even_odd_count(0))  # ==> (1, 0)
# print(even_odd_count(7895643210))  # ==> (5, 3)
#