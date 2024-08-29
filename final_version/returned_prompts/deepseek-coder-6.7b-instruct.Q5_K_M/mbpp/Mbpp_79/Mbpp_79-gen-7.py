
def word_len(word):
    return len(word) % 2 != 0

print(word_len("Hadoop"))  # False

"""
This function works by taking in a word and using the len() function to find the length of the word. The modulo operator (%) is then used to find the remainder of the length divided by 2. If the remainder is not 0, it means that the length of the word is an odd number, so the function returns True. If the remainder is 0, it means that the length of the word is an even number, so the function returns False.
"""
<jupyter_output>
False
<jupyter_text>
Question 2
<jupyter_code>
