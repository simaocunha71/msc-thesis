    # You can either use a dictionary to store the extensions and their strength
    # or you can use a list of tuples to store the extensions and their strength.
    # The list of tuples is easier to work with, so we'll do that here.
    extensions_with_strength = []
    for extension in extensions:
        strength = 0
        for c in extension:
            if c.isupper():
                strength -= 1
            else:
                strength += 1
        extensions_with_strength.append((strength, extension))

    # Now we have a list of tuples, each containing a strength and an extension
    # We want to sort the list by strength
    extensions_with_strength.sort(reverse=True)
    # Now we have the strongest extension at the beginning of the list
    # We return it in the format ClassName.StrongestExtensionName
    return f'{class_name}.{extensions_with_strength[0][1]}'


