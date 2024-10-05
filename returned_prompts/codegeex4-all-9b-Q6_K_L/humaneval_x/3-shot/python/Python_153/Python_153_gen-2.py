    strongest_extension = extensions[0]
    strongest_strength = 0

    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm

        if strength > strongest_strength:
            strongest_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"