    extensions_strength = [sum(1 for c in extension if c.isupper()) - sum(1 for c in extension if c.islower()) for extension in extensions]
    strongest_extension = extensions[extensions_strength.index(max(extensions_strength))]
    return f"{class_name}.{strongest_extension}"


