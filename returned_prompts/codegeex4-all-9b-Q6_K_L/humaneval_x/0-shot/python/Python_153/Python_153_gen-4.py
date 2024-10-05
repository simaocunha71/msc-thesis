def Strongest_Extension(class_name, extensions):
    def strength(e):
        return sum(1 for c in e if c.isupper()) - sum(1 for c in e if c.islower())
    best = max(extensions, key=strength)
    return '%s.%s' % (class_name, best)

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))