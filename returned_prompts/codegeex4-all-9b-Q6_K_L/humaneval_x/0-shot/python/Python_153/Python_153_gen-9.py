def Strongest_Extension(class_name, extensions):
    strongest = extensions[0]
    for ext in extensions:
        if sum(1 for c in ext if c.isupper()) - sum(1 for c in ext if c.islower()) > sum(1 for c in strongest if c.isupper()) - sum(1 for c in strongest if c.islower()):
            strongest = ext
    return class_name + '.' + strongest

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))