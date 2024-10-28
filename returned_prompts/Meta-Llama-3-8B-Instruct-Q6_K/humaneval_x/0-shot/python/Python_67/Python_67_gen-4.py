    # Split the input string to get the number of apples and oranges
    fruit_info = s.split(' ')
    apples = int(fruit_info[1].split(' ')[0])
    oranges = int(fruit_info[3].split(' ')[0])

    # Calculate the total number of fruits in the basket
    total_fruits = int(n)

    # Calculate the number of mango fruits in the basket
    mangoes = total_fruits - apples - oranges

    return mangoes
    



# Test cases
print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
print(fruit_distribution("4 apples and 5 oranges", 200))  # Output: 191
print(fruit_distribution("10 apples and 20 oranges", 300))  # Output: 270
print(fruit_distribution("1 apple and 2 oranges", 10))  # Output: 7
print(fruit_distribution("50 apples and 30 oranges", 1000))  # Output: 920
print(fruit_distribution("3 apples and 4 oranges", 15))  # Output: 8
print(fruit_distribution("9 apples and 10 oranges", 20))  # Output: 1
print(fruit_distribution("7 apples and 8 oranges", 30))  # Output: 15
print(fruit_distribution("0 apples and 0 oranges", 5))  # Output: 5
print(fruit_distribution("1 apple and 1 orange", 3))  # Output: 1
print(fruit_distribution("5 apples and 5 oranges", 15))  # Output: 5
print(fruit_distribution("1 apple and 2 oranges", 10))  # Output: 7
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120))  # Output: 19
print(fruit_distribution("4 apples and 5 oranges", 200))  # Output: 191
print(fruit_distribution("10 apples