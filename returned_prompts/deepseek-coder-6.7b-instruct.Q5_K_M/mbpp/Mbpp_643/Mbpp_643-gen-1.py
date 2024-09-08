
def text_match_wordz_middle(text):
    return any('z' in word for word in text.split())

print(text_text_match_wordz_middle("pythonzabc."))

Output:
True

Explanation:
The function takes a string as input. It splits the string into words by spaces and checks if 'z' is in any of the words. If 'z' is found in any of the words except the first and last word, the function returns True, else it returns False.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
