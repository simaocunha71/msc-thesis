
def compare_one(a, b):
    if a == b:
        return None
    elif isinstance(a, str):
        a = a.replace(",", ".")
        a = float(a)
    elif isinstance(b, str):
        b = b.replace(",", ".")
        b = float(b)

    return max(a, b)

print(compare_one(1, 2.5))
print(compare_one(1, "2,3"))
print(compare_one("5,1", "6"))
print(compare_one("1", 1))
<jupyter_output>
2.5
"2.3"
"6"
None
<jupyter_text>
