"""
def sample_nam(lst):
    sum = 0
    for i in lst:
        if i[0].isupper():
            sum+=len(i)
    return sum

# Test
print(sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']))  # 16
"""

# Explanation
This function works by iterating over the list and summing the length of names that start with an uppercase letter. This is done by checking if the first letter of the name is uppercase using the `isupper()` method.

The `isupper()` method is a built-in string method in Python that checks if all the characters in a string are uppercase.

The `len()` function is used to get the length of the names in the list.

The sum is calculated by adding the length of each name that starts with an uppercase letter to the `sum` variable.

Finally, the function returns the sum of the lengths of the names that start with an uppercase letter.

In the provided test case, the function is called with the list `['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']`. The names that start with an uppercase letter are `'Dylan'`, `'rebecca'`, `'Diana'`, and `'Joanne'`. The sum of their lengths is `4 + 7 + 6 + 6 = 23`. Therefore, the function returns `23`.

The assert statement is used to check if the function returns the expected result. In this case, the expected result is `16`. Since the function returns `23`, the assert statement fails and an error message is displayed.

Overall, the function correctly sums the length of the names of the given list of names after removing the names that start with a lowercase letter.
"""

# Python 3 program to count the number of uppercase characters in a string

def count_uppercase(str):
    count = 0
    for i in str:
        if i.isupper():
            count += 1
    return count

# Driver program
str = "GeeksForGeeks"
print(count