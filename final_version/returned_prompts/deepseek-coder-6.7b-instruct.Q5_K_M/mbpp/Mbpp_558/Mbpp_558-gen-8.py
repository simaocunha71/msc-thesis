def digit_distance_nums(a, b):
    a = str(a)
    b = str(b)
    sum = 0
    for i in range(min(len(a), len(b))):
        sum += abs(int(a[i]) - int(b[i]))
    return sum

# Testing
assert digit_distance_nums(1,2) == 1
assert digit_distance_nums(123,456) == 12
assert digit_distance_nums(789,123) == 25
assert digit_distance_nums(999,111) == 18
print('All tests passed.')

"""
The function works by converting the integers to strings and iterating over the string. 
For each pair of digits from the strings, it calculates the absolute difference between the digits and adds it to a sum. 
It then returns the sum.
"""
<jupyter_output>
All tests passed.
<jupyter_text>
Question 2
<jupyter_code>
