def count_char_position(s):
    count = 0
    s = s.lower()
    for i in range(len(s)):
        if s[i] == chr(97+i):
            count += 1
    return count

print(count_char_position("xbcefg"))

# Output: 2

# Explanation:
# The character at position 0 in the string "xbcefg" is 'x'. It is also the 0th character in the English alphabet (0-based index).
# The character at position 1 in the string "xbcefg" is 'b'. It is also the 1st character in the English alphabet.
# However, the character at position 2 in the string "xbcefg" is 'c', which is the 2nd character in the English alphabet, but it does not match the 2nd character of the string "xbcefg".
# So, the function returns 2.
<jupyter_output>
2
<jupyter_text>
3. Write a function to check whether a string is a palindrome or not. A palindrome is a word, phrase, number, or other sequences of characters that reads the same backward as forward.
<jupyter_code>
