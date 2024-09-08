
def word_len(word):
    return len(word) % 2 != 0

print(word_len("Hadoop"))

# Output: False

"""
Explanation:
The function `word_len` takes a word as an argument and returns the result of the modulo operation of the length of the word with 2. If the result is not 0, it means the length of the word is an odd number, so the function returns True. If the result is 0, it means the length of the word is an even number, so the function returns False.
"""
<jupyter_output>
False
<jupyter_text>
Question 2:Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
<jupyter_code>
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))
# Output: 120
<jupyter_output>
120
<jupyter_text>
Question 3:Write a Python function that takes a list of numbers and returns a list with the squares of the numbers in the original list.
<jupyter_code>
def square_numbers(nums):
    return [num ** 2 for num in nums]

print(square_numbers([1, 2, 3, 4, 5]))
# Output: [1, 4, 9, 16, 25]
<jupyter_output>
[1, 4, 9, 16, 25]
<jupyter_text>
Question 4:Write a Python function that takes a string and returns a new string with all the vowels removed.
<jupyter_code>
def remove_vowels(string):
    vowels = 'aeiouAEIOU'
    return ''.join([char for char in string if char not in vowels])

print(remove_vowels("Hello, World!"))
# Output: "Hll, Wr