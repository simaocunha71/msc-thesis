def snake_to_camel(s):
    s = s.replace('_', '')
    return ''.join(word.capitalize() for word in s.split())