from typing import List

def concatenate(strings: List[str]) -> str:
    result = ''
    for string in strings:
        result += string
    return result
# or use the join method
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)  # This is a more Pythonic way to do it. It is more concise and efficient.