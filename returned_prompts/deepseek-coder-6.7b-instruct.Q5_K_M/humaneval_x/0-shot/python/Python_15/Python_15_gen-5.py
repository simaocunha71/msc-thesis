

def string_sequence(n: int) -> str:
    return " ".join(str(i) for i in range(n+1))


print(string_sequence(0))
print(string_sequence(5))


The solution uses a generator expression to create a sequence of numbers from 0 to n (inclusive), then the join method is used to convert these numbers into a single string with spaces in between.

"""

# %%

# 