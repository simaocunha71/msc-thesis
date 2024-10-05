
def Strongest_Extension(class_name, extensions):
    extensions.sort(key=lambda x: (len(x), -sum(ord(c) - ord('a') + 1 for c in x.lower())))
    return class_name + '.' + extensions[0]
