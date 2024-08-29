def text_match_wordz_middle(text):
    for i in range(1, len(text) - 1):
        if text[i] == 'z':
            return True
    return False

print(text_match_wordz_middle("pythonzabc."))

# Output: True

"""
Explanation:
The function text_match_wordz_middle takes a string input text. It loops through each character in the text, except for the first and last characters. If it finds a 'z' it returns True. If it doesn't find any 'z' it returns False.
"""
<jupyter_output>
True
<jupyter_text>
Problem 3:
<jupyter_code>
