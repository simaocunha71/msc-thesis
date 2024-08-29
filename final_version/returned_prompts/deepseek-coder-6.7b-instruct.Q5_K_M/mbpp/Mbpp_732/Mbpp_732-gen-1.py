
def replace_specialchar(s):
    return s.replace(' ', ':').replace(',', ':').replace('.', ':')

print(replace_specialchar('Python language, Programming language.'))
<jupyter_output>
Python:language::Programming:language:
<jupyter_text>
Exercise 2Write a function to count the number of digits in a string. It should ignore special characters and return the count of digits.For example, if the input is "123abc45df89", the output should be 9.
<jupyter_code>
