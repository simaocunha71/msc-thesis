def fruit_distribution(s,n):
    # Split the input string to get the number of apples and oranges
    fruits = s.split()
    apples = int(fruits[0])
    oranges = int(fruits[4])

    # Calculate the number of mangoes
    mangoes = n - apples - oranges

    return mangoes

# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19)) # 8
print(fruit_distribution("0 apples and 1 oranges",3)) # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges",120)) # 19