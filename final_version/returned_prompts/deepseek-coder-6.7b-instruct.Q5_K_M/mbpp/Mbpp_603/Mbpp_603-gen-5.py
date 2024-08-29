def get_ludic(n):
    ludics = [1]
    i = 2
    while True:
        if i * 2 - 1 > n:
            break
        ludics.append(i * 2 - 1)
        i += 1
    return ludics

assert get_ludic(10) == [1, 2, 3, 5, 7]
"""
The function get_ludic(n) returns all the Lucas numbers that are smaller than or equal to n. The Lucas numbers are defined by the recurrence relation L(n) = L(n-1) + L(n-2), where the initial conditions are L(0) = 2 and L(1) = 1.

In the while loop, we keep adding the next Lucas numbers until we reach a number that exceeds n. The next Lucas number is calculated as (current number * 2) - 1.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
