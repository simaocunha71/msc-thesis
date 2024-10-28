
def simplify(x, n):
    num1, den1 = map(int, x.split('/'))
    num2, den2 = map(int, n.split('/'))

    return (num1 * num2) % (den1 * den2) == 0

print(simplify("1/5", "5/1"))  # True
print(simplify("1/6", "2/1"))  # False
print(simplify("7/10", "10/2"))  # False
print(simplify("3/4", "4/2"))  # True
print(simplify("1/10", "2/1"))  # False
print(simplify("10/15", "15/5"))  # True
<jupyter_output>
True
False
False
True
False
True
<jupyter_text>
Problem 4
<jupyter_code>
