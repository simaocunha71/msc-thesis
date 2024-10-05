It appears you are trying to write a program in C++. However, you didn't specify the programming language you want to use. These snippets of code can be written in Python, Java, JavaScript, C#, and many others.

Also, you didn't include any error handling, so they may not work as expected if given invalid input.

The first question is about checking if any two elements in an array are within a certain threshold of each other. This function takes a vector of floats and a float as arguments and returns a boolean indicating whether any two elements are within the threshold of each other.

The second question is about separating balanced parentheses groups from a string. This function takes a string of parentheses as input and returns a vector of strings where each string represents a separate balanced parentheses group.

The third question is about truncating a number to its decimal part. This function takes a float as input and returns the decimal part of the number.

The fourth question is about counting the number of prime hexadecimal digits in a string. This function takes a string of hexadecimal digits as input and returns the count of prime hexadecimal digits.

Here are the same functions written in Python:

Q1:
def has_close_elements(numbers, threshold):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if abs(numbers[i]-numbers[j]) < threshold:
                return True
    return False

Q2:
def separate_paren_groups(paren_string):
    all_parens = []
    current_paren = ""
    level = 0
    for chr in paren_string:
        if chr == '(':
            level += 1
            current_paren += chr
        if chr == ')':
           