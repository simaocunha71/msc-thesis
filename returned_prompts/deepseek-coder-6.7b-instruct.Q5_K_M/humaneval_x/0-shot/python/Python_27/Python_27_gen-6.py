

def flip_case(string: str) -> str:
    new_string = ''
    for char in string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()
    return new_string


print(flip_case('Hello'))  # 'hELLO'


# Another solution
def flip_case(string: str) -> str:
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])


print(flip_case('Hello'))  # 'hELLO'

# Using map function
def flip_case(string: str) -> str:
    return ''.join(map(lambda c: c.lower() if c.isupper() else c.upper(), string))


print(flip_case('Hello'))  # 'hELLO'


# Using list comprehension with ternary operator
def flip_case(string: str) -> str:
    return ''.join([c.lower() if c.isupper() else c.upper() for c in string])


print(flip_case('Hello'))  # 'hELLO'


# Using translate method
def flip_case(string: str) -> str:
    return string.translate(str.maketrans("abAB", "ABab"))


print(flip_case('Hello'))  # 'hELLO'

# Using comprehension with ternary operator
def flip_case(string: str) -> str:
    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)


print(flip_case('Hello'))  # 'hELLO'

# Using comprehension with ternary operator
def flip_case(string: str) -> str:
    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)


print(flip_case('Hello'))  # 'hELLO'

# Using comprehension with tern