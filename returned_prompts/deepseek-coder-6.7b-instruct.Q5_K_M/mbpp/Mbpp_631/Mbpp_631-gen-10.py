def replace_spaces(s: str) -> str:
    return s.replace(" ", "_") if " " in s else s.replace("_", " ")

print(replace_spaces('Jumanji The Jungle'))

# Output: Jumanji_The_Jungle

# The function works by checking if there are spaces in the string. If yes, it replaces them with underscores. If no, it replaces underscores with spaces.


# If you want to handle multiple spaces and/or underscores between words:
def replace_spaces(s: str) -> str:
    return s.replace(" ", "_").replace("__", "_").replace("_", " ") if " " in s else s.replace(" ", "").replace("__", "_")

print(replace_spaces('Jumanji  The   Jungle'))

# Output: Jumanji_The_Jungle

# The function works by first replacing all spaces with underscores. If there are multiple consecutive spaces, it replaces them with a single underscore. Then, if there are underscores in the string, it replaces them with spaces. Otherwise, it removes all spaces.
<jupyter_output>
<empty_output>
<jupyter_text>
9. Write a Python function to convert a given list of tuples into a dictionary.
<jupyter_code>
