
    def Strongest_Extension(class_name, extensions):
        strongest = 0
        strongest_extension = None
        for extension in extensions:
            cap = sum(1 for c in extension if c.isupper())
            sm = sum(1 for c in extension if c.islower())
            strength = cap - sm
            if strength > strongest:
                strongest = strength
                strongest_extension = extension
        return f"{class_name}.{strongest_extension}"

    print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))

