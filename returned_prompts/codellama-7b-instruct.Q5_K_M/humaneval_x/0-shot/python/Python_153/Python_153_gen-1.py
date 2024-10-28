
    # sort the extensions by their strength
    extensions.sort(key=lambda extension: extension_strength(extension))

    # return the strongest extension
    return f'{class_name}.{extensions[0]}'

def extension_strength(extension_name):
    """Calculates the strength of an extension.
    The strength is given by the fraction of the number of uppercase letters in the
    extension's name and the number of lowercase letters.
    For example, an extension named 'AaBbCc' would have a strength of 2/3.
    """
    uppercase_letters = len([c for c in extension_name if c.isupper()])
    lowercase_letters = len([c for c in extension_name if c.islower()])

    return uppercase_letters - lowercase_letters
