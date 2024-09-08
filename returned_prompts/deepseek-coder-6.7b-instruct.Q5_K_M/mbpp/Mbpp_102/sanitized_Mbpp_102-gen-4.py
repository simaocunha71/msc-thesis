def snake_to_camel(s):
    s = s.split('_')
    return ''.join(i.title() for i in s)