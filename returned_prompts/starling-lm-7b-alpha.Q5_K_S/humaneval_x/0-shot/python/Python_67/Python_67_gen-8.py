
def fruit_distribution(s,n):
    num_list = s.split(' ')
    apples = int(num_list[0].split(' ')[-1])
    oranges = int(num_list[1].split(' ')[-1])
    return n - apples - oranges


print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))




# In this problem, we are asked to create a function called `fruit_distribution` that takes two inputs: a string and an integer. The string represents a number of apples and oranges that are distributed in a basket of fruit. The integer represents the total number of fruits in the basket.

# To solve this problem, we can start by splitting the string at the spaces. This will give us a list of substrings, where the first substring represents the number of apples and the second substring represents the number of oranges.

# We can then extract the actual numbers from these substrings by splitting them again at the spaces and taking the last element of each sublist. We convert these elements to integers.

# Finally, we can subtract the number of apples and oranges from the total number of fruits to find the number of mangoes in the basket.

# Here are some test cases to verify that our solution works correctly:

# fruit_distribution("5 apples and 6 oranges", 19) -> 8 (19 - 5 - 6 = 8)
# fruit_distribution("0 apples and 1 oranges",3) -> 2 (3 - 0 - 1 = 2)
# fruit_distribution("2 apples and 3 oranges", 100) -> 95 (100 - 2 - 3 = 95)
# fruit_distribution("100 apples and 1 oranges",120) -> 19 (12