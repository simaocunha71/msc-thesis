    strongest_extension = extensions[0]
    strongest_extension_strength = sum(1 for c in extensions[0] if c.isupper()) - sum(1 for c in extensions[0] if c.islower())

    for extension in extensions:
        extension_strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())

        if extension_strength > strongest_extension_strength:
            strongest_extension = extension
            strongest_extension_strength = extension_strength

    return f"{class_name}.{strongest_extension}"