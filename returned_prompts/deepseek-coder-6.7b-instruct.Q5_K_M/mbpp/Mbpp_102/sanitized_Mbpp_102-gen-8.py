def snake_to_camel(s):
    return ''.join(word.title() for word in s.split('_'))