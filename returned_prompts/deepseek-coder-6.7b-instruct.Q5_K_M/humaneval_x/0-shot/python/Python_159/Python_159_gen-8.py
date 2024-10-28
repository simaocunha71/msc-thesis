
def eat(number, need, remaining):
    if need > remaining:
        return [number + remaining, 0]
    else:
        return [number + need, remaining - need]

print(eat(5, 6, 10))
print(eat(4, 8, 9))
print(eat(1, 10, 10))
print(eat(2, 11, 5))


# Output:
# [11, 4]
# [12, 1]
# [11, 0]
# [7, 0]
<jupyter_output>
<empty_output>
<jupyter_text>
12. Write a Python function to find the maximum and minimum value in a list. The function should return the maximum and minimum as a list [max, min].
<jupyter_code>
