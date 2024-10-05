def fruit_distribution(s,n):
    # Split the string into words
    words = s.split()

    # Find the indices of 'apples' and 'oranges'
    apples_index = words.index('apples')
    oranges_index = words.index('oranges')

    # Extract the numbers of apples and oranges
    apples = int(words[apples_index - 1])
    oranges = int(words[oranges_index - 1])

    # Calculate the number of mangoes
    mangoes = n - apples - oranges

    return mangoes

print(fruit_distribution("5 apples and 6 oranges", 19)) # 8
print(fruit_distribution("0 apples and 1 oranges",3)) # 2
print(fruit_distribution("2 apples and 3 oranges", 100)) # 95
print(fruit_distribution("100 apples and 1 oranges",120)) # 19