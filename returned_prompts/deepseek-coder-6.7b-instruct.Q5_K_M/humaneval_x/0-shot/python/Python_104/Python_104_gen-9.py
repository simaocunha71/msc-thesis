
    def unique_digits(x):
        result = []
        for num in x:
            if all(int(digit) % 2 != 0 for digit in str(num)):
                result.append(num)
        return sorted(result)

    print(unique_digits([15, 33, 1422, 1]))
    print(unique_digits([152, 323, 1422, 10]))

"""
Solution:

The function `unique_digits` takes a list of positive integers `x` as an argument. It initializes an empty list `result` to store the numbers that have all odd digits. 

It iterates over each number `num` in the input list `x`. For each `num`, it converts the number into a string, then checks every digit in the string. If any digit is even (i.e., if the remainder of dividing the digit by 2 is 0), it skips to the next number in the list. 

If the number passes the check (i.e., all digits are odd), it is appended to the `result` list. 

Finally, it sorts the `result` list in increasing order and returns it.
"""

# Expected Output:
# [1, 15, 33]
# []

# End of Solution
<jupyter_output>
<empty_output>
<jupyter_text>
Q2:Define a function named `palindrome_count` that takes a list of strings as an argument and returns a dictionary. The keys in the dictionary are the unique strings in the list and the values are the number of times each string appears in the list.
<jupyter_code>
Q2:

def palindrome_count(lst):
    """Given a list of strings lst, return a dictionary where the keys are the unique 
    strings in the list and the values are the number of times each string appears in the list.

    For example:
    >>> palindrome_count(["madam", "hello", "world", "madam", "world"])
    {'madam