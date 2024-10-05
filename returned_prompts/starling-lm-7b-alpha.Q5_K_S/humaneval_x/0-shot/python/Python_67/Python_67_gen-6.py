    # first, I'll split the string by the space
    fruits = s.split(" ")
    # then, I'll create an empty list to store the numbers
    fruits_list = []
    # for every fruit, I'll check if it's an apple or an orange
    for i in range(len(fruits)):
        # if the word is apple
        if "apples" in fruits[i]:
            # I'll split it by the word apples
            fruits_list.append(int(fruits[i].split(" ")[1]))
        elif "oranges" in fruits[i]:
            # if the word is oranges
            # I'll split it by the word oranges
            fruits_list.append(int(fruits[i].split(" ")[1]))
    # now, I'll calculate the total number of apples and oranges
    total = sum(fruits_list)
    # and return the number of mangos which is the difference between the total number
    # of fruits and the total number of apples and oranges
    return n - total

# I'll call the function with the examples
print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))























































































































































