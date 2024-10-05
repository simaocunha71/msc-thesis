    extensions_strengths = [(ext, len(ext) - len(ext.lower())) for ext in extensions]
    max_strength = max(ext_strength[1] for ext_strength in extensions_strengths)
    extensions_with_max_strength = [ext for ext, strength in extensions_strengths if strength == max_strength]
    return f'{class_name}.{extensions_with_max_strength[0]}'


