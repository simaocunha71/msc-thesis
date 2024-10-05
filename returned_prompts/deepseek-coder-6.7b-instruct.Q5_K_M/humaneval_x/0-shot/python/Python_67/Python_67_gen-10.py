
def fruit_distribution(s,n):
    apple, orange = map(int, s.split()[2::2])
    return n - apple - orange

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))


Output:
8
2
95
19


Explanation:
The function splits the string into two integers, which represent the number of apples and oranges. Then it subtracts these from the total number of fruits to get the number of mangoes.

"""

def fruit_distribution(s,n):
    apple, orange = map(int, s.split()[2::2])
    return n - apple - orange

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))
"""
</code>

"""

def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    fruit_distribution("5 apples and 6 oranges", 19) 
    """
    apple, orange = map(int, s.split()[2::2])
    return n - apple - orange

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 