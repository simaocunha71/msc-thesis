
def Strongest_Extension(class_name, extensions):
    strongest_extension = ''
    strength = 0
    for extension in extensions:
        extension_strength = 0
        for char in extension:
            if char.isupper():
                extension_strength += 1
        if extension_strength > strength:
            strength = extension_strength
            strongest_extension = extension
    return class_name + '.' + strongest_extension