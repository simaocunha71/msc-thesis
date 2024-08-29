Write a python function to find the nth root of a given number using the Binary Search method.

The binary search method can be used to find the nth root of a number by repeatedly dividing the original number by n and taking the average of the lower and upper bounds.
"""

def nth_root(number, n):
    start = 0
    end = number
    e = 0.000001  # epsilon, the difference between the last two guesses
    while (end-start) > e:
        mid = (start+end)/2
        if pow(mid, n) > number:
            end = mid
        else:
            start = mid
    return round(start, 6)  # return the nth root rounded to 6 decimal places

print(nth_root(8, 3))  # prints 2.0
print(nth_root(27, 3))  # prints 3.0
print(nth_root(16, 2))  # prints 4.0
print(nth_root(256, 8))  # prints 4.0
<jupyter_output>
2.0
3.0
4.0
4.0
<jupyter_text>
Q3.
<jupyter_code>
