def concatenate(strings: List[str]) -> str:
    result = ""
    for string in strings:
        result += string
    return result

# Test cases
print(concatenate([]))  # Output: ''
print(concatenate(['a', 'b', 'c']))  # Output: 'abc'
print(concatenate(['hello', 'world']))  # Output: 'helloworld'  # Output: 'helloworld'  # Output: 'helloworld'
print(concatenate(['a', 'b', 'c', 'd', 'e']))  # Output: 'abcde'  # Output: 'abcde'
print(concatenate(['hello', 'world', 'python']))  # Output: 'helloworldpython'  # Output: 'helloworldpython'
print(concatenate(['a', 'b', 'c', 'd', 'e', 'f']))  # Output: 'abcdef'  # Output: 'abcdef'
print(concatenate(['hello', 'world', 'python', 'programming']))  # Output: 'helloworldpythonprogramming'  # Output: 'helloworldpythonprogramming'
print(concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g']))  # Output: 'abcdefg'  # Output: 'abcdefg'
print(concatenate(['hello', 'world', 'python', 'programming', 'is']))  # Output: 'helloworldpythonprogrammingis'  # Output: 'helloworldpythonprogrammingis'  # Output: 'helloworldpythonprogrammingis'  # Output: 'helloworldpythonprogrammingis'
print(concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']))  # Output: 'abcdefgh'  # Output: 'abcdefgh'  # Output: 'abcdefgh'
print(concatenate(['hello', 'world', 'python', 'programming', 'is', 'fun']))  # Output: 'helloworldpythonprogrammingisfun'  # Output: 'helloworldpythonprogrammingisfun'
print(concatenate(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']))  # Output: 'abcdefghi'  # Output: 'abcdefghi'
print(concatenate(['hello', 'world', 'python', 'programming', 'is', 'fun', 'because']))  # Output: 'helloworldpythonprogrammingisfunbeca  #