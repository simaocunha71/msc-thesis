    if not extensions:
        return class_name

    strongest_extension = extensions[0]
    strongest_extension_strength = -1 * len(strongest_extension.lower()) + len(strongest_extension.upper())

    for extension in extensions:
        extension_strength = -1 * len(extension.lower()) + len(extension.upper())

        if extension_strength > strongest_extension_strength:
            strongest_extension_strength = extension_strength
            strongest_extension = extension

    return f'{class_name}.{strongest_extension}'


