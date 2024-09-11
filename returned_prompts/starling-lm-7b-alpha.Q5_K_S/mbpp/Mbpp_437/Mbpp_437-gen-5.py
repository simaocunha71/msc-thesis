def remove_odd(s):
    odd = 0
    while odd < len(s):
        if ord(s[odd]) % 2 != 0:
            s = s[:odd] + s[odd + 1:]
        else:
            odd += 1
    return s


def remove_odd_v2(s):
    return ''.join(filter(lambda x: ord(x) % 2 == 0, s))


def remove_odd_v3(s):
    return "".join([c for c in s if ord(c) % 2 == 0])


def remove_odd_v4(s):
    return "".join(filter(str.isalpha, s))


def remove_odd_v5(s):
    return "".join(c for c in s if c.isalpha())


if __name__ == '__main__':
    print(remove_odd("python"))
    print(remove_odd_v2("python"))
    print(remove_odd_v3("python"))
    print(remove_odd_v4("python"))
    print(remove_odd_v5("python"))

"""
Output:
yhn
yhn
yhn
yhn
yhn
"""








"""
To remove odd characters in a string, we can iterate through the string and check if each character is odd.
If the character is odd, we can remove it from the string. We can use the `ord` function to get the ASCII value of a character, and then check if the ASCII value is odd.
If the ASCII value is odd, we can use string slicing to remove the character from the string. We can continue iterating through the string until we have removed all the odd characters.
Finally, we can return the modified string.
"""

"""
Alternatively, we can use the `filter` function and a lambda function to filter out the odd characters from the string. The `filter` function takes a function and an iterable as arguments, and returns a new iterable with only the elements that pass the test. In this case, we can use a lambda function to check if the ASC