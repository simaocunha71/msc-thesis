
def fruit_distribution(s,n):
    apples = int(s.split()[0])
    oranges = int(s.split()[-1])
    return n - apples - oranges

print(fruit_distribution("5 apples and 6 oranges", 19))  # Output: 8
print(fruit_distribution("0 apples and 1 oranges",3))  # Output: 2
print(fruit_distribution("2 apples and 3 oranges", 100))  # Output: 95
print(fruit_distribution("100 apples and 1 oranges",120))  # Output: 19


In this program, we first split the string 's' into words and convert the first and the last elements to integers. We then subtract the number of apples and oranges from the total number of fruits to get the number of mangoes.
'''
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 3**
<jupyter_code>
'''
