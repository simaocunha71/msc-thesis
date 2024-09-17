def extract_string(strings, length):
    return [string for string in strings if len(string) >= length]
strings = ['Python', 'list', 'exercises', 'practice', 'solution']
length = 8