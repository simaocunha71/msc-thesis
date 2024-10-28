
    return all([item.islower() if item.isalpha() else True for item in dict.keys()]) or all([item.isupper() if item.isalpha() else True for item in dict.keys()])