    class_name = str(class_name)
    extensions = list(extensions)
    strongest_extension = extensions[0]
    strongest_strength = len([c for c in extensions[0] if c.isupper()]) - len([c for c in extensions[0] if c.islower()])

    for extension in extensions:
        strength = len([c for c in extension if c.isupper()]) - len([c for c in extension if c.islower()])

        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength

    return class_name + '.' + strongest_extension