def snake_to_camel(s):
    words = s.split('_')
    return ''.join(word.capitalize() for word in words)