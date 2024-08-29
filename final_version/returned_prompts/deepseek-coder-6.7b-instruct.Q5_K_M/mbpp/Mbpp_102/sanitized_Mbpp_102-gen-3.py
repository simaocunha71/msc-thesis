def snake_to_camel(s):
    words = s.split('_')
    return ''.join(word.title() for word in words)