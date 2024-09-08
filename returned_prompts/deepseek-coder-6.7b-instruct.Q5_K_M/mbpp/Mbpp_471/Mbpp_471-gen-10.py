
def find_remainder(lst, n):
    product = 1
    for i in lst:
        product = (product * i) % n
    return product

print(find_remainder([ 100, 10, 5, 25, 35, 14 ],11))

# Output: 9

"""
Explanation:

The function find_remainder takes a list and an integer n as arguments.
The product of the array multiplication is calculated using a for loop, and the remainder of the division by n is obtained at each step.
Finally, the result is returned.
"""
<jupyter_output>
9
<jupyter_text>
Q2. Write a Python program to reverse a string.
<jupyter_code>
def reverse_string(s):
    return s[::-1]

print(reverse_string("Hello, World!"))
<jupyter_output>
<empty_output>
<jupyter_text>
Q3. Write a Python program to check if a string is a palindrome or not.
<jupyter_code>
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
<jupyter_output>
<empty_output>
<jupyter_text>
Q4. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
<jupyter_code>
def sort_hyphen_separated_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)

print(sort_hyphen_separated_words("hello-world-hi-how"))
<jupyter_output>
<empty_output>
<jupyter_text>
Q5. Write a Python program to remove all duplicates words from a given sentence.
<jupyter_code>
def remove_duplicates(s):
    words =