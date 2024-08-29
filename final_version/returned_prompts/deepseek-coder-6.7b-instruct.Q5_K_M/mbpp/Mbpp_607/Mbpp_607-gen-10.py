
def find_literals(text, pattern):
    match = re.search(pattern, text)
    if match:
        return match.group(), match.start(), match.end()
    else:
        return None

print(find_literals('The quick brown fox jumps over the lazy dog.', 'fox'))

# Output: ('fox', 16, 19)

"""
This function uses the re.search function to search the given text for the given pattern. The function re.search() returns a match object if the text matches the pattern. The match object has several methods that can be used to retrieve information about the match, including the matched substring, the starting index and the ending index of the match. If the text does not match the pattern, the function returns None.
"""
<jupyter_output>
('fox', 16, 19)
<jupyter_text>
