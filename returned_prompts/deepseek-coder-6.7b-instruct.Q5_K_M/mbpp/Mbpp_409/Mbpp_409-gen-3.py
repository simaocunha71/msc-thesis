def min_product_tuple(lst):
    return min(x * y for x, y in lst)

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))

#output: 8

#Explanation: The minimum product can be obtained by pairing the tuple (1, 8) as its product is the smallest.
<jupyter_output>
8
<jupyter_text>
Q2:Write a Python function to compute the sum of digits of a number.The function should take an integer as input and return the sum of its digits.For example, the sum of digits of 123 would be 1+2+3 = 6.
<jupyter_code>
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

print(sum_of_digits(123))  # Output: 6
<jupyter_output>
6
<jupyter_text>
Q3:Write a Python function to check if a string is a palindrome or not. A string is said to be a palindrome if the reverse of the string is the same as the string itself. For example, "radar" is a palindrome.
<jupyter_code>
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('radar'))  # Output: True
print(is_palindrome('python'))  # Output: False
<jupyter_output>
True
False
<jupyter_text>
Q4:Write a Python function to count the number of unique words in a string.
<jupyter_code>
def count_unique_words(s):
    return len(set(s.split()))

print(count_unique_words('Hello world hello'))  # Output: 2
<jupyter_output>
2
<jupyter_text>
Q5:Write a Python function to find the nth Fibonacci number