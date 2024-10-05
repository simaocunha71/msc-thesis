    class_name = class_name
    extensions = extensions

    strengths = []
    for extension in extensions:
        cap = sum(c.isupper() for c in extension)
        sm = sum(c.islower() for c in extension)
        strengths.append(cap - sm)

    strongest_index = strengths.index(max(strengths))
    return "{}.{}".format(class_name, extensions[strongest_index])


