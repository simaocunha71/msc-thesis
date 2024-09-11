def capitalize_first_letter(s):
    words = s.split(" ")
    result = []
    for w in words:
        result.append(w[0].upper() + w[1:])
    return " ".join(result)

# assert capitalize_first_letter("python") == "Python"
# assert capitalize_first_letter("hello world") == "Hello World"
# assert capitalize_first_letter("i love python") == "I Love Python"
# assert capitalize_first_letter("") == ""

"""
Given a string, return a dictionary with all the unique characters in the string as keys and their respective counts as values.

Examples:

char_count("Hello") ➞ {'H': 1, 'e': 1, 'l': 2, 'o': 1}
char_count("Python") ➞ {'P': 1, 'y': 1, 't': 1, 'o': 1, 'n