    class_strengths = {}

    for extension in extensions:
        class_strengths[extension] = 0

        for c in extension:
            if c.isupper():
                class_strengths[extension] += 1

    strongest_extension = max(class_strengths, key=lambda x: class_strengths[x])

    return class_name + '.' + strongest_extension


