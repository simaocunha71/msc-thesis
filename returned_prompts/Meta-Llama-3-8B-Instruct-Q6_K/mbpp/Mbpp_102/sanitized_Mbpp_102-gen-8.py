def snake_to_camel(s):
    components = s.split('_')
    return ''.join(x.title() for x in components) if s else ''
    # or
    # return ''.join(x.capitalize() for x in components) if s else ''
    # or
    # return ''.join(x.capitalize() for x in components[1:]) + components[0] if s else ''
    # or
    # return ''.join(x.capitalize() for x in components[1:]) + components[0].lower() if s else ''