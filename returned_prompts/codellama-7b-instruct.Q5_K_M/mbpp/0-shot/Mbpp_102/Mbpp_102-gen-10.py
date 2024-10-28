def snake_to_camel(s):
    return s[0].lower() + ''.join(x.title() for x in s.split('_')[1:])
