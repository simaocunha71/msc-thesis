    extensions.sort(key=lambda x: (len([c for c in x if c.isupper()]) - len([c for c in x if c.islower()]), x), reverse=True)
    return class_name + "." + extensions[0]


