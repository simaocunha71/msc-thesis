def Strongest_Extension(class_name, extensions):
    def strength(extension_name):
        return sum(1 for c in extension_name if c.isupper()) - sum(1 for c in extension_name if c.islower())

    strongest = max(extensions, key=strength)
    return f'{class_name}.{strongest}'

print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))  # 'my_class.AA'