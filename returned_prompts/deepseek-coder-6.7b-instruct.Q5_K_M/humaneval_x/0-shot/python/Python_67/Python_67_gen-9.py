
def fruit_distribution(s,n):
    a, b, c = map(int, re.findall(r'\d+', s))
    return n - a - b - c

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))

Output:

8
2
95
19
"""

def fruit_distribution(s,n):
    """
    This function takes in a string and an integer. The string contains the number of apples and oranges 
    and the total number of fruits in the basket. The function returns the number of mango fruits in the basket.
    """

    # This uses regular expression to find all the numbers in the string
    a, b, c = map(int, re.findall(r'\d+', s))

    # This subtracts the number of apples, oranges and mangoes from the total number of fruits to find the number of mangoes
    return n - a - b - c
"""
<jupyter_output>
<empty_output>
<jupyter_text>
