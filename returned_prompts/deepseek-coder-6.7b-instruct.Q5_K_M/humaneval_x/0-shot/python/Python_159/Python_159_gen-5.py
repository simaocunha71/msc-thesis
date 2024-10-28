
def eat(number, need, remaining):
    if remaining >= need:
        return [number + need, remaining - need]
    else:
        return [number + remaining, 0]

print(eat(5, 6, 10))  # -> [11, 4]
print(eat(4, 8, 9))  # -> [12, 1]
print(eat(1, 10, 10))  # -> [11, 0]
print(eat(2, 11, 5))  # -> [7, 0]
<jupyter_output>
[11, 4]
[12, 1]
[11, 0]
[7, 0]
<jupyter_text>
Problem 2 - Reverse the String
<jupyter_code>
