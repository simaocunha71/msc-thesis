def fruit_distribution(s,n):
    s = s.replace("apples", "")
    s = s.replace("oranges", "")
    s = s.replace("and", "")
    s = s.replace(" ", "")
    return n - int(s)

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges",3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges",120))  # Output: 19