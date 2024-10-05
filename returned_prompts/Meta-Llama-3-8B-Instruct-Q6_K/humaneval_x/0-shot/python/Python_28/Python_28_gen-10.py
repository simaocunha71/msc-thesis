from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string """
    result = ''
    for s in strings:
        result += s
    return result

# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['hello', 'world']))  # 'helloworld'
print(concatenate(['a', 'b', 'c', 'd', 'e']))  # 'abcde'







from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string """
    return ''.join(strings)  # use the join method

# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['hello', 'world']))  # 'helloworld'
print(concatenate(['a', 'b', 'c', 'd', 'e']))  # 'abcde'
print(concatenate(['abc', 'def', 'ghi']))  # 'abcdefghi'







from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string """
    result = ''
    for s in strings:
        result += s
    return result

# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['hello', 'world']))  # 'helloworld'
print(concatenate(['a', 'b', 'c', 'd', 'e']))  # 'abcde'
print(concatenate(['abc', 'def', 'ghi']))  # 'abcdefghi'

# Alternative solution using the join method
def concatenate(strings: List[str]) -> str:
    return ''.join(strings)  # use the join method

# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'
print(concatenate(['hello', 'world']))  # 'helloworld'
print(concatenate(['a', 'b', 'c', 'd', 'e']))  # 'abcde'
print(concatenate(['abc', 'def', 'ghi']))  # 'abcdefghi'







from typing import List

def concatenate(strings: List[str]) -> str:
    """ Concatenate list