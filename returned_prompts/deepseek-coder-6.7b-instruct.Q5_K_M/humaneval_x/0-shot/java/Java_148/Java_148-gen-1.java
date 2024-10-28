
    s = s.split()
    apples = int(s[0]) + int(s[4])
    oranges = int(s[6])
    return n - apples - oranges


print(fruit_distribution("5 apples and 6 oranges", 19))  # 8
print(fruit_distribution("0 apples and 1 oranges",3))  # 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # 95
print(fruit_distribution("100 apples and 1 oranges",120))  # 19


# The code works by splitting the input string into a list of words, then converting the apples and oranges 
# from strings to integers and adding them together. The total number of fruits in the basket is then 
# subtracted from this sum to get the number of mangoes.
<jupyter_output>
8
2
95
19
<jupyter_text>
1.2. Write a Python function that takes a list of numbers and returns a new list with all the elements of the first list in reverse order.
<jupyter_code>
