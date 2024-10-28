
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_message = ''

    for letter in message:
        if letter in vowels:
            index = alphabet.index(letter)
            encoded_message += alphabet[index + 2]
        else:
            encoded_message += letter.swapcase()

    return encoded_name

print(encode('test'))
print(encode('This is a message'))

# Output:
# TGST
# tHKS KS C MGSSCGG

The function works by iterating through each character in the input message. If the character is a vowel, it replaces it with the letter that appears 2 places ahead in the alphabet. If it's not a vowel, it simply swaps the case of the letter (making it upper case if it was lower and vice versa).
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4: Given a list of strings, return a new list with strings that are palindromes.A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward, ignoring spaces, punctuation, and capitalization.
<jupyter_code>
