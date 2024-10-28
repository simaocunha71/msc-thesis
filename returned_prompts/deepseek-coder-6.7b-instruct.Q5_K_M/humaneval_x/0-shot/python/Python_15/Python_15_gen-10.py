

def string_sequence(n: int)  -> str:
    return " ".join(str(i) for i in range(n+1))

print(string_sequence(0))
print(string_sequence(5))


# ------
# Solution 2: Using list comprehension
# ------

