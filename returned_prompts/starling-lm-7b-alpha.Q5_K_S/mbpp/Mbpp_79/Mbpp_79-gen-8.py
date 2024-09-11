def word_len(word):
    if len(word) % 2 == 0:
        return True
    else:
        return False

word_len("Hadoop")







"""
def word_len(word):
    if len(word) % 2 == 0:
        return True
    else:
        return False

# To check the function
print(word_len("Hadoop"))  # Expected: False
"""

# In Python, we can use the modulo operator % to check if a number is odd or even.
# If the modulo of the number with 2 is equal to 0, then the number is even, otherwise it is odd.

# Here, we define a function called word_len that takes a word as input. Inside the function, we use the len() function to get the length of the word. We then use the modulo operator % to check if the length of the word is divisible by 2. If it is, we return True, otherwise we return False.

# To check the function, we call it with the word "Hadoop" as input. According to the definition of the function, since the length of "Hadoop" is 7 (which is an odd number), the function should return False. We can verify this by printing the result of the function call.

"""
In the given Python code, a function named 'word_len' is defined to check if the length of a given word is odd or not. The function takes a single argument, 'word', which represents the input word.

Inside the function, the length of the word is calculated using the 'len()' function. This length is then checked using the modulo operator '%' to see if it is divisible by 2. If the length is divisible by 2, the function returns True, indicating that the length is even. Otherwise, it returns False, indicating that the length is odd.

To test the function, it is called with the word "Hadoop" as the input. According to the function's definition, since the length of "Hadoop" is 7 (which is an odd number), the function should return False. This result is printed to the console.
"""

"""
Here's a step