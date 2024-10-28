
def fruit_distribution(s,n):
    apples, oranges = map(int, [i for i in s.split() if i.isdigit()])
    return n - apples - oranges

print(fruit_distribution("5 apples and 6 oranges", 19))
print(fruit_distribution("0 apples and 1 oranges",3))
print(fruit_distribution("2 apples and 3 oranges", 100))
print(fruit_distribution("100 apples and 1 oranges",120))

The function fruit_distribution takes a string and an integer as inputs. The string is split into a list of words and the digits are extracted into apples and oranges. Then it returns the difference between the total number of fruits and the number of apples and oranges.

The print statements at the end are just to test the function with the examples you provided.
<jupyter_output>
<empty_output>
<jupyter_text>
Exercise 2
<jupyter_code>
