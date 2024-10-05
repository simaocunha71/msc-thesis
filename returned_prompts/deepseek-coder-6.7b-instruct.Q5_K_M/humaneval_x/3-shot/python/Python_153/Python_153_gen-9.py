    strongest_extension = extensions[0]
    highest_strength = sum([1 for c in strongest_extension if c.isupper()]) - sum([1 for c in strongest_extension if c.islower()])

    for extension in extensions[1:]:
        strength = sum([1 for c in extension if c.isupper()]) - sum([1 for c in extension if c.islower()])
        if strength > highest_strength:
            strongest_extension = extension
            highest_strength = strength

    return f"{class_name}.{strongest_extension}"


