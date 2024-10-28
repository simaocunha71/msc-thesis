
    import hashlib

    if text == "":
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()

print(string_to_md5("Hello world"))
assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'

# Explanation: 
# The function uses hashlib library's md5 method to convert the text to its md5 hash equivalent.
# If the text is an empty string, it returns None.
# The encode() function is used to convert the string into bytes to be hashed.
# The hexdigest() function then returns the md5 hash as a hexadecimal string.
<jupyter_output>
3e25960a79dbc69b674cd4ec67a72c62
<jupyter_text>
Question 2: Write a function named 'get_most_common_words' that takes a string 'text' and an integer 'n' as arguments. The function should return a list of the 'n' most common words in 'text'. If 'n' is greater than the number of unique words in 'text', return all words sorted by frequency.
<jupyter_code>
