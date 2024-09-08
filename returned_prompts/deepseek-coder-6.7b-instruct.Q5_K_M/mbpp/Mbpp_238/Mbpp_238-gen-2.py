def number_of_substrings(s):
    n = len(s)
    return n * (n + 1) // 2

print(number_of_substrings("abc"))  # 6

Explanation:
We are given a string of length n.
A substring can be of any length from 1 to n.
For each substring of length 1, there is only 1 substring.
For each substring of length 2, there are 2 substrings, and so on.
For substrings of length n, there are n substrings.
The sum of all substrings of length 1 to n is n * (n + 1) / 2.
So, the total number of non-empty substrings of the given string is n * (n + 1) / 2.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
3. Write a Python program to convert a string to datetime
<jupyter_code>
# Python program to convert string to datetime
from datetime import datetime

def convert_string_to_datetime(date_string):
    date_object = datetime.strptime(date_string, '%d %m %Y')
    return date_object

date_string = '16 08 2022'
print(convert_string_to_datetime(date_string))
<jupyter_output>
2022-08-16 00:00:00
<jupyter_text>
4. Write a Python program to get the current date and time
<jupyter_code>
# Python program to get the current date and time
from datetime import datetime

current_datetime = datetime.now()
print("Current date and time:", current_datetime)
<jupyter_output>
Current date and time: 2022-08-16 12:31:41.090106
<jupyter_text>
5. Write a Python program to subtract five days from current date
<jupyter_code>
# Python program to subtract five days from current date
