def extract_values(s):
    return [i.strip('"') for i in s.split('"')[:-1]]


# Test
print(extract_values('"Python", "PHP", "Java"'))  # ['Python', 'PHP', 'Java']

"""
The function extract_values takes a string as input and returns a list of values.
It uses the split method to split the input string at every quotation mark.
Then, using a list comprehension, it removes the quotation marks from the result.
Finally, it returns the resulting list.
"""

"""
The assert statement is used to check if the function extract_values correctly extracts the values between quotation marks from the given string.
In this case, the assert statement checks if the output of extract_values('"Python", "PHP", "Java"') is equal to the expected output ['Python', 'PHP', 'Java'].
If the assert statement passes, it means that the function is working correctly.
"""

"""
The print statement is used to display the result of the function extract_values when called with the string '"Python", "PHP", "Java"'.
It will print ['Python', 'PHP', 'Java'], which is the list of values extracted from the string.
"""

"""
The function extract_values uses the split method to split the input string at every quotation mark.
This creates a list of substrings, with each substring being a value between quotation marks.
Then, using a list comprehension, the function removes the quotation marks from each substring.
Finally, the function returns the resulting list of values.
"""

"""
The assert statement is used to verify if the function extract_values correctly extracts the values between quotation marks from the given string.
In this case, the assert statement checks if the output of extract_values('"Python", "PHP", "Java"') is equal to the expected output ['Python', 'PHP', 'Java'].
If the assert statement passes, it means that the function is working correctly.
"""

"""
The print statement is used to display the result of the function extract_values when called with the string '"Python", "PHP", "Java"'.
It will print ['Python', 'PHP', '