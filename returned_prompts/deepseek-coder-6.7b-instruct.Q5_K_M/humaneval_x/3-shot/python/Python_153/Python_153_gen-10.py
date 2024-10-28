    strongest_name = extensions[0]
    strongest_strength = sum([name.isupper() for name in extensions[0]]) - sum([name.islower() for name in extensions[0]])

    for extension in extensions[1:]:
        strength = sum([extension.isupper() for extension in extension]) - sum([extension.islower() for extension in extension])
        if strength > strongest_strength:
            strongest_name = extension
            strongest_strength = strength

    return f"{class_name}.{strongest_name}"


