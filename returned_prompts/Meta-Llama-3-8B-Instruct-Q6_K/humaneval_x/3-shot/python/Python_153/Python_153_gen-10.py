    strongest_extension = None
    strongest_extension_strength = float('-inf')

    for extension in extensions:
        uppercase = sum(1 for c in extension if c.isupper())
        lowercase = sum(1 for c in extension if c.islower())
        strength = uppercase - lowercase

        if strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = strength

    return f"{class_name}.{strongest_extension}"


