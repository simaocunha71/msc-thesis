from typing import List

def concatenate(strings: List[str]) -> str:
    result = ''
    for s in strings:
        result += s
    return result
# test cases
assert concatenate([]) == ''
assert concatenate(['a', 'b', 'c']) == 'abc'
assert concatenate(['hello', 'world']) == 'helloworld'
assert concatenate(['', '']) == ''
assert concatenate(['', 'hello']) == 'hello'  # empty string should be ignored
assert concatenate(['a', '', 'c']) == 'ac'  # empty string should be ignored
assert concatenate(['a', 'b', 'c', 'd']) == 'abcd'  # multiple strings
assert concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']) == 'abcdefghij'  # many strings
assert concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']) == 'abcdefghijklmnopqrstuvwxyz'  # many strings
assert concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) == 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  # many strings
assert concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w