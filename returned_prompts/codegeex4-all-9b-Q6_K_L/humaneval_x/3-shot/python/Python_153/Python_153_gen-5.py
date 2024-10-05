    max_strength = float('-inf')
    max_name = ''
    for extension in extensions:
        strength = sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower())
        if strength > max_strength:
            max_strength = strength
            max_name = extension
    return f'{class_name}.{max_name}'