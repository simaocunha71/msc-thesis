def Strongest_Extension(class_name, extensions):
    strongest = extensions[0]
    for extension in extensions:
        if extension.count('A') - extension.count('a') > strongest.count('A') - strongest.count('a'):
            strongest = extension
    return class_name + '.' + strongest

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))