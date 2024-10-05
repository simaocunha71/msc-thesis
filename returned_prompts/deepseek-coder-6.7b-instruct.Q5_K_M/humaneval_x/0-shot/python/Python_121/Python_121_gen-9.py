
    return sum(i for i in lst[::2] if i % 2 != 0)

print(solution([5, 8, 7, 1]))
print(solution([3, 3, 3, 3, 3]))
print(solution([30, 13, 24, 321]))
<jupyter_output>
12
9
0
<jupyter_text>
**Problem 2:** Given an integer list, return a list of the same length where each element is the sum of all the integers in the input list excluding the integer at the current position.
<jupyter_code>
