def snake_to_camel(s):
    if not s:
        return s
    components = s.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
    # return ''.join(x.capitalize() or y for x, y in zip(components, ('', components[1:])))
    # return ''.join(x.capitalize() for x in components)  # This will also work but not as per the requirement