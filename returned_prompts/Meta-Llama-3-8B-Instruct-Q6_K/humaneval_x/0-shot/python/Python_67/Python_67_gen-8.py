    # Split the string into two parts, one for the number of apples and one for the number of oranges
    apple_orange = s.split(' and ')
    
    # Extract the number of apples and oranges
    apple = int(apple_orange[0].split(' ')[0])
    orange = int(apple_orange[1].split(' ')[0])
    
    # Calculate the total number of fruits
    total = n
    
    # Calculate the number of mango fruits by subtracting the number of apples and oranges from the total
    mango = total - apple - orange
    
    return mango

# Testing the function
print(fruit_distribution("5 apples and 6 oranges", 19)) # Output: 8
print(fruit_distribution("0 apples and 1 oranges", 3)) # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # Output: 95
print(fruit_distribution("100 apples and 1 oranges", 120)) # Output: 19
print(fruit_distribution("50 apples and 20 oranges", 200)) # Output: 30
print(fruit_distribution("1 apples and 2 oranges", 5)) # Output: 2
print(fruit_distribution("3 apples and 4 oranges", 15)) # Output: 8
print(fruit_distribution("0 apples and 0 oranges", 10)) # Output: 10
print(fruit_distribution("1 apples and 1 oranges", 5)) # Output: 3
print(fruit_distribution("2 apples and 2 oranges", 10)) # Output: 6
print(fruit_distribution("0 apples and 0 oranges", 5)) # Output: 5
print(fruit_distribution("100 apples and 100 oranges", 300)) # Output: 100
print(fruit_distribution("50 apples and 50 oranges", 150)) # Output: 50
print(fruit_distribution("0 apples and 0 oranges", 10)) # Output: 10
print(fruit_distribution("1 apples and 1 oranges", 5)) # Output: 3
print(fruit_distribution("2 apples and 2 oranges", 10)) # Output: 6
print(fruit_distribution("0 apples and 0 oranges", 5)) # Output: 5
print(fruit_distribution("100 apples and 100 oranges", 300)) # Output: 100
print(fruit_distribution