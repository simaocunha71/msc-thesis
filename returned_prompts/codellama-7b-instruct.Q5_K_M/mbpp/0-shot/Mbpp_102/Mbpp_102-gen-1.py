"""
def snake_to_camel(snake_case_string):
    components = snake_case_string.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'capitalize' method and join them together.
    return components[0] + "".join(x.capitalize() for x in components[1:])
"""
