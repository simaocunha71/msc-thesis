    def strength(extension):
        cap = sum(1 for c in extension if c.isupper())
        sm = sum(1 for c in extension if c.islower())
        return cap - sm

    extensions.sort(key=strength, reverse=True)
    return class_name + '.' + extensions[0]


