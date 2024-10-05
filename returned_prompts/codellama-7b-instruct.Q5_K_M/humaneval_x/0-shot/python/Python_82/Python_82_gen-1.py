
def prime_length(string):
    if len(string) == 0:
        return False
    for i in range(2, len(string)+1):
        if len(string) % i == 0:
            if i == len(string):
                return True
            else:
                return False


# 2.
# Write a function that takes a string and returns True if the string
# contains only spaces or if the string is empty, False otherwise

def string_spaces(string):
    if len(string) == 0:
        return True
    for char in string:
        if char != ' ':
            return False
    return True


# 3.
# Write a function that takes a string and returns the string with all
# the vowels removed.

def remove_vowels(string):
    vowels = 'aeiou'
    new_string = ''
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string


# 4.
# Write a function that takes a string and returns a new string with all
# the words reversed.

def reverse_words(string):
    words = string.split(' ')
    new_string = ''
    for word in words:
        new_string += word[::-1] + ' '
    return new_string.strip()


# 5.
# Write a function that takes a string and returns True if the string
# contains only spaces or if the string is empty, False otherwise

def string_spaces(string):
    if len(string) == 0:
        return True
    for char in string:
        if char != ' ':
            return False
    return True


# 6.
# Write a function that takes a string and returns the string with all
# the vowels removed.

def remove_vowels(string):
    vowels = 'aeiou'
    new_string = ''
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string


# 7.
# Write