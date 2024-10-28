
def Strongest_Extension(class_name, extensions):
    extension_strengths = []
    for extension in extensions:
        cap_count = sum(1 for c in extension if c.isupper())
        sm_count = sum(1 for c in extension if c.islower())
        extension_strengths.append(cap_count - sm_count)
    strongest_extension_index = extension_strengths.index(max(extension_strengths))
    return f'{class_name}.{extensions[strongest_extension_index]}'


