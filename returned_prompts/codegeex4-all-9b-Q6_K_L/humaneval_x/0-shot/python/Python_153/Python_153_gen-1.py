def Strongest_Extension(class_name, extensions):
    strongest = extensions[0]
    for extension in extensions:
        if sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower()) > sum(1 for c in strongest if c.isupper()) - sum(1 for c in strongest if c.islower()):
            strongest = extension

    return class_name + '.' + strongest

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC'])) # 'my_class.AA'