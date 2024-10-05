from typing import List

def concatenate(strings: List[str]) -> str:
    result = ""
    for s in strings:
        result += s
    return result
# or
def concatenate(strings: List[str]) -> str:
    return "".join(strings)

# Testing the function
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'







