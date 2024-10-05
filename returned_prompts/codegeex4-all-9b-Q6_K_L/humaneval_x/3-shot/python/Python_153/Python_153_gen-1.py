    strongest_extension = extensions[0]
    strongest_strength = 0

    for extension in extensions:
        strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())
        if strength > strongest_strength:
            strongest_strength = strength
            strongest_extension = extension

    return class_name + '.' + strongest_extension

