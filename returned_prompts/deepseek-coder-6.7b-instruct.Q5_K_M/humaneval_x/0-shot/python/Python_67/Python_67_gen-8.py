
def fruit_distribution(s,n):
    apples = int(s.split("apples")[0].split("and")[1].strip())
    oranges = int(s.split("and")[2].split("oranges")[0].strip())
    return n - apples - oranges

print(fruit_distribution("5 apples and 6 oranges", 19)) #8
print(fruit_distribution("0 apples and 1 oranges",3)) #2
print(fruit_distribution("2 apples and 3 oranges", 100)) #95
print(fruit_distribution("100 apples and 1 oranges",120)) #19


# You can use the split() function to split the input string into words and then parse the 
# numbers you are interested in. The total number of fruits, minus the number of apples and 
# oranges, is the number of mangoes.

# In the first example, the number of apples is 5, the number of oranges is 6, and the 
# total number of fruits is 19. Subtracting 5 and 6 from 19 gives 8, so there are 8 
# mangoes in the basket.

# In the second example, the number of apples is 0, the number of oranges is 1, and the 
# total number of fruits is 3. Subtracting 0 and 1 from 3 gives 2, so there are 2 
# mangoes in the basket.

# In the third example, the number of apples is 2, the number of oranges is 3, and the 
# total number of fruits is 100. Subtracting 2 and 3 from 100 gives 95, so there are 95 
# mangoes in the basket.

# In the fourth example, the number of apples is 100, the number of oranges is 1, and the 
# total number of fruits is 120. Subtracting 100 and 1 from 120 gives 19, so there are 19 
# mangoes in the basket.

#