
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

print(eat(5, 6, 10))
print(eat(4, 8, 9))
print(eat(1, 10, 10))
print(eat(2, 11, 5))
<jupyter_output>
[11, 4]
[12, 1]
[11, 0]
[7, 0]
<jupyter_text>
**Exercise 7**: Write a function that takes a number and returns its factorial.  For example, if you input 5, the function should return 120.
<jupyter_code>
