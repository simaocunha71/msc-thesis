
def fruit_distribution(s,n):
    num_apples = int(s.split()[0])
    num_oranges = int(s.split()[2])
    return n - num_apples - num_oranges

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))

This will split the string on spaces and take the first number, third number as the number of apples and oranges respectively. Then it subtracts the total number of apples and oranges from the total number of fruits to find the number of mangoes.
"""

#Q2:
"""
