from typing import List

def concatenate(strings: List[str]) -> str:
    result = ''
    for string in strings:
        result += string
    return result

# Test cases
print(concatenate([]))  # ''
print(concatenate(['a', 'b', 'c']))  # 'abc'  # Correct
print(concatenate(['hello', 'world']))  # 'helloworld'  # Correct
print(concatenate(['a', 'b', 'c', 'd']))  # 'abcd'  # Correct
print(concatenate(['1', '2', '3']))  # '123'  # Correct
print(concatenate(['a', 'b']))  # 'ab'  # Correct
print(concatenate(['hello', '']))  # 'hello'  # Correct
print(concatenate(['', 'hello']))  # 'hello'  # Correct
print(concatenate(['']))  # ''  # Correct
print(concatenate(['a']))  # 'a'  # Correct
print(concatenate(['']))  # ''  # Correct
print(concatenate([]))  # ''  # Correct

# Note: You can also use the join() function in Python
# def concatenate(strings: List[str]) -> str:
#     return ''.join(strings)  # Correct
# print(concatenate(['a', 'b', 'c']))  # 'abc'  # Correct
# print(concatenate(['hello', 'world']))  # 'helloworld'  # Correct
# print(concatenate(['a', 'b', 'c', 'd']))  # 'abcd'  # Correct
# print(concatenate(['1', '2', '3']))  # '123'  # Correct
# print(concatenate(['a', 'b']))  # 'ab'  # Correct
# print(concatenate(['hello', '']))  # 'hello'  # Correct
# print(concatenate(['', 'hello']))  # 'hello'  # Correct
# print(concatenate(['']))  # ''  # Correct
# print(concatenate(['a']))  # 'a'  # Correct
# print(concatenate(['']))  # ''  # Correct
# print(concatenate([]))  # ''  # Correct
# This is another way to achieve the same result
# The join() function concatenates all the elements in a list into a single string.
# The elements are separated by the string provided as the first argument.
