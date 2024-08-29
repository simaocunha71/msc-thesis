def digit_distance_nums(a,b):
    return sum(abs(int(x) - int(y)) for x, y in zip(str(a), str(b)))

# Test Cases
print(digit_distance_nums(1,2)) # 1
print(digit_distance_nums(123,321)) # 12
print(digit_distance_nums(24,42)) # 6

# This program works by first converting the two input integers to strings. 
# Then, it iterates over the digits of the two strings in parallel (using zip), 
# calculating the absolute difference between the corresponding digits (using abs and int), 
# and summing them up (using sum).
<jupyter_output>
1
12
6
<jupyter_text>
