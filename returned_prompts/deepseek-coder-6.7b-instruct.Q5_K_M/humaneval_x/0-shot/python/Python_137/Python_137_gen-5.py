
def compare_one(a, b):
    # Checking if the types of a and b are the same
    if type(a) != type(b):
        return None
    if type(a) == str:
        a = a.replace(',', '.')
        b = b.replace(',', '.')
        a = float(a)
        b = float(b)
    if a == b:
        return None
    return max(a, b)

print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
print(compare_one(2.5, 2.5))
<jupyter_output>
2.5
2.3
6.0
None
2.5
<jupyter_text>
Problem 2
<jupyter_code>
