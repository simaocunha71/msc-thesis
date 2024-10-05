
def fruit_distribution(s,n):
    a, b = map(int, [i for i in s.split() if i.isdigit()])
    return n - a - b

print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges",3))  # 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # 95
print(fruit_distribution("100 apples and 1 oranges",120))  # 19


# 2. Task:
# Create a function named "greetings" that returns the string "Hello, <name> how are you doing today?"
# where <name> is the string that is passed to the function.
# For example:
# greetings("John") -> "Hello, John how are you doing today?"

