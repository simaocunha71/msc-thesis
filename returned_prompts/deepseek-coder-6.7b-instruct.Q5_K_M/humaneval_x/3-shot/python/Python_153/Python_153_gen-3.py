    strongest_extension = extensions[0]
    max_strength = sum(c.isupper() for c in strongest_extension) - sum(c.islower() for c in strongest_extension)

    for extension in extensions[1:]:
        strength = sum(c.isupper() for c in extension) - sum(c.islower() for c in extension)
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension

    return f"{class_name}.{strongest_extension}"


