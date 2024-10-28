    strengths = {ext: sum([ext.count(c) for c in ext if c.isupper()]
                          ) - sum([ext.count(c) for c in ext if c.islower()]) for ext in extensions}
    strongest_extension = max(strengths, key=strengths.get)
    return f'{class_name}.{strongest_extension}'

