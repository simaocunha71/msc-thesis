    extensions_strength = {}
    for ext in extensions:
        strength = sum([ord(c) - ord('a') for c in ext if c.islower()]) - \
            sum([ord(c) - ord('A') for c in ext if c.isupper()])
        extensions_strength[ext] = strength
    return class_name + '.' + max(extensions_strength, key=extensions_strength.get)


