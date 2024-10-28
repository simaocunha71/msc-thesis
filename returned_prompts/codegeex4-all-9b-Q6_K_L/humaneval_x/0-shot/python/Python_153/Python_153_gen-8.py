def Strongest_Extension(class_name, extensions):
    def strength(ext):
        return sum(1 for c in ext if c.isupper()) - sum(1 for c in ext if c.islower())
    strongest = max(extensions, key=strength)
    return class_name + '.' + strongest

print Strongest_Extension('my_class', ['AA', 'Be', 'CC'])