    strongest_extension = extensions[0]
    strongest_strength = sum(1 for c in extensions[0] if c.isupper()) - sum(1 for c in extensions[0] if c.islower())

    for extension in extensions:
        strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())
        if strength > strongest_strength:
            strongest_extension = extension
            strongest_strength = strength

    return f"{class_name}.{strongest_extension}"