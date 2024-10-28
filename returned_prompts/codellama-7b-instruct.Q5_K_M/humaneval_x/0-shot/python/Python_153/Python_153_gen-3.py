
    def Strongest_Extension(class_name, extensions):
        strongest = 0
        best_extension = ""
        for extension in extensions:
            cap = 0
            sm = 0
            for char in extension:
                if char.isupper():
                    cap += 1
                elif char.islower():
                    sm += 1
            strength = cap - sm
            if strength > strongest:
                strongest = strength
                best_extension = extension
        return class_name + "." + best_extension


