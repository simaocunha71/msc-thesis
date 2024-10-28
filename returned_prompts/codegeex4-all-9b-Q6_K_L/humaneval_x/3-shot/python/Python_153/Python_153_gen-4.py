    max_strength = -len(class_name)
    strongest_extension = class_name

    for extension in extensions:
        strength = len([c for c in extension if c.isupper()]) - len([c for c in extension if c.islower()])

        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f'{class_name}.{strongest_extension}'


