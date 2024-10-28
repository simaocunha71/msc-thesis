    strongest_extension = extensions[0]
    max_strength = 0

    for extension in extensions:
        strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())

        if strength > max_strength:
            strongest_extension = extension
            max_strength = strength

    return f"{class_name}.{strongest_extension}"