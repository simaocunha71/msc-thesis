    extensions_with_strength = [(extension, len(re.findall('[A-Z]', extension))) for extension in extensions]
    extensions_with_strength = [(extension, strength) for (extension, strength) in extensions_with_strength if strength > 0]
    sorted_extensions = sorted(extensions_with_strength, key=lambda x: x[1], reverse=True)

    return f"{class_name}.{sorted_extensions[0][0]}"


