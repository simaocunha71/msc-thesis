def replace_blank(s, char):
    return s.replace(" ", char)  # Using the replace() function of the string
    # or
    # return s.translate({ord(' '): char})  # Using the translate() function of the string and ord() function of the built-in functions
    # or
    # return s.replace(" ", char).replace("\t", char).replace("\n", char)  # For replacing all kinds of whitespace characters