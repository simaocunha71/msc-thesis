

def flip_case(string: str) -> str:
    return ''.join(char.upper() if char.islower() else char.lower() for char in string)


print(flip_case('Hello'))  # Output: hELLO


# Alternatively, you could use a list comprehension to flip the case:

def flip_case(string: str) -> str:
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])


print(flip_case('Hello'))  # Output: hELLO


# Or, you could use the map() function with a lambda function:

def flip_case(string: str) -> str:
    return ''.join(map(lambda char: char.upper() if char.islower() else char.lower(), string))


print(flip_case('Hello'))  # Output: hELLO


# You could also use the translate() method with a translation table:

def flip_case(string: str) -> str:
    return string.translate(str.maketrans('abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'))


print(flip_case('Hello'))  # Output: hELLO


# Finally, you could use a for loop to flip the case:

def flip_case(string: str) -> str:
    result = ''
    for char in string:
        if char.islower():
            result += char.upper()
        else:
            result += char.lower()
    return result


print(flip_case('Hello'))  # Output: hELLO


# In all these implementations, the time complexity is O(n) and the space complexity is O(n), where n is the length of the string.


```














