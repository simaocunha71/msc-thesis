from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))

The function filter_by_substring uses a list comprehension to iterate over the input list strings and include only the ones that contain the substring.

Here is a similar solution using a normal for loop:

```python
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    result = []
    for string in strings:
        if substring in string:
            result.append(string)
    return result
```
'''

# Test cases:
print(filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a'))
print(filter_by_substring(['hello', 'world', 'python', 'is', 'awesome'], 'o'))
print(filter_by_substring(['I', 'love', 'coding', 'in', 'Python'], 'o'))
print(filter_by_substring(['apple', 'orange', 'banana', 'cherry', 'grape'], 'a'))
print(filter_by_substring(['code', 'python', 'java', 'javascript'], 'a'))
<jupyter_output>
['abc', 'bacd', 'array']
['hello', 'world', 'python', 'awesome']
['I', 'love', 'coding', 'Python']
['apple', 'orange', 'grape']
['code', 'python', 'java', 'javascript']
<jupyter_text>
Question 3:
<jupyter_code>
'''
