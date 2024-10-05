    max_strength = -float('inf')
    strongest_extension = None
    for extension in extensions:
        upper = sum(1 for c in extension if c.isupper())
        lower = sum(1 for c in extension if c.islower())
        strength = upper - lower
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f"{class_name}.{strongest_extension}"


