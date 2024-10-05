
    class_name = class_name.lower()
    extensions = [ext.lower() for ext in extensions]
    strongest = -1
    strongest_extension = None
    for extension in extensions:
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        strength = cap - sm
        if strength > strongest:
            strongest = strength
            strongest_extension = extension
    return '{0}.{1}'.format(class_name, strongest_extension)
