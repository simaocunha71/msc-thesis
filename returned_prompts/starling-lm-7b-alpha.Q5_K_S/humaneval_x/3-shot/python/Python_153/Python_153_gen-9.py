    class_name = class_name.lower()
    extensions = [extension.lower() for extension in extensions]
    strengths = []
    for extension in extensions:
        cap_count = sum([1 for char in extension if char.isupper()])
        sm_count = sum([1 for char in extension if char.islower()])
        strengths.append(cap_count - sm_count)
    strongest_index = strengths.index(max(strengths))
    return class_name + '.' + extensions[strongest_index]


