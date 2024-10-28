
    def Strongest_Extension(class_name, extensions):
        max_strength = -1
        strongest_extension = ""
        for extension in extensions:
            strength = extension.lower().count("a") - extension.upper().count("A")
            if strength > max_strength:
                max_strength = strength
                strongest_extension = extension
        return class_name + "." + strongest_extension


