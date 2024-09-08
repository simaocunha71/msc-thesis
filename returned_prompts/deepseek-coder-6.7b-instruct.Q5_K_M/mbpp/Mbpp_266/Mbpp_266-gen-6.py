
def lateralsurface_cube(side_length):
    return 4 * side_length ** 2

print(lateralsurface_cube(5))

# Output: 100
<jupyter_output>
100
<jupyter_text>
Q2.Write a Python function that takes a string as an input and returns the number of vowels in the string. The function should be case-insensitive.
<jupyter_code>
def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string.lower():
        if char in vowels:
            count += 1
    return count

string = 'Hello World'
print(count_vowels(string)) # Output: 3
<jupyter_output>
3
<jupyter_text>
Q3.Write a Python function that takes a list of integers and returns the sum of the squares of the odd integers in the list.
<jupyter_code>
def sum_square_odd(lst):
    return sum(i**2 for i in lst if i%2 != 0)

lst = [1, 2, 3, 4, 5]
print(sum_square_odd(lst)) # Output: 35
<jupyter_output>
35
<jupyter_text>
Q4.Write a Python function that takes a string as an input and returns True if it's a palindrome and False otherwise. A string is considered a palindrome if it's the same when read forwards and backwards. The function should ignore spaces, punctuation, and capitalization.
<jupyter_code>
def is_palindrome(string):
    string = ''.join(char for char in string if char.isalnum()).lower()
    return string == string[::-1]

string = 'A man, a plan, a canal: Panama'
print(is_palindrome(string)) # Output: True
<jupyter_output>
True
<jupyter_text>
Q5.Write