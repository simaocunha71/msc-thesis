def snake_to_camel(s):
    return ''.join(x.capitalize() or '_' for x in s.split('_'))

