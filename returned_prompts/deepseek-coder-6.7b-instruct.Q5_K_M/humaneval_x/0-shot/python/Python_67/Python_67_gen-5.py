
def fruit_distribution(s,n):
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    """
    apples = int(s.split("apples")[0].split(" ")[1])
    oranges = int(s.split("and")[1].split(" ")[2])
    return n - apples - oranges

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))
<jupyter_output>
8
2
95
19
<jupyter_text>
3. Write a function named `count_characters` that takes a string as an input and returns a dictionary where the keys are the characters in the string and the values are the number of times each character appears in the string.
<jupyter_code>
