    # Get list of lowercase and uppercase letters in each extension name
    # Get the length of each list
    # Sort list of extensions by length, if same length, sort alphabetically
    # Return class name followed by strongest extension
    # If there are multiple strongest, return first one

    # Get list of uppercase and lowercase letters in each extension name
    extension_info = [(x.lower(), x.upper()) for x in extensions]

    # Sort list of extensions by length, if same length, sort alphabetically
    extension_info.sort(key=lambda x: (-len(x[0]), x[1]))

    # Get class name and strongest extension
    class_name, strongest_extension = extension_info[0]

    # Return class name followed by strongest extension
    return class_name + "." + strongest_extension


