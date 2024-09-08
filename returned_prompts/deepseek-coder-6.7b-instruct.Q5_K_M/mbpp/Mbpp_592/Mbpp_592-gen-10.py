
def binomial_product(n):
    product = 1
    for i in range(n):
        product *= (n-i)*(n-i-1)//(i+1)
    return product

def sum_Of_product(n):
    return sum(binomial_product(i) for i in range(1,n+1))

print(sum_Of_product(3))

# Expected output: 15
<jupyter_output>
15
<jupyter_text>
Q2: Write a Python program to convert a given list of strings into a list of lists where each string is represented as a list of characters.
<jupyter_code>
# Input: ['abc', 'def', 'ghi']
# Output: [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

def convert_to_list(lst):
    return [list(i) for i in lst]

print(convert_to_list(['abc', 'def', 'ghi']))
<jupyter_output>
[['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
<jupyter_text>
Q3: Write a Python program to check if a given string is a palindrome or not.
<jupyter_code>
# Input: 'madam'
# Output: True

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome('madam'))
<jupyter_output>
True
<jupyter_text>
Q4: Write a Python program to implement a stack using a linked list.
<jupyter_code>
class Node: 
    def __init__(self, data=None): 
        self.data = data
        self.next = None

class Stack: 
    def __init__(self): 
        self.top = None

    def push(self, data): 
        if self.top is None: 
            self