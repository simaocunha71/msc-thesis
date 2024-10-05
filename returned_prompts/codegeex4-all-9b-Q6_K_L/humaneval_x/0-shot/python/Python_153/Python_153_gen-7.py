def Strongest_Extension(class_name, extensions):
    strongest = extensions[0]
    strength = sum(1 for c in strongest if c.isupper()) - sum(1 for c in strongest if c.islower())
    for extension in extensions[1:]:
        s = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())
        if s > strength:
            strongest = extension
            strength = s
    return class_name + '.' + strongest

print Strongest_Extension('my_class', ['AA', 'Be', 'CC']) # == 'my_class.AA'