    strengths = [(extension, sum([1 for c in extension if c.isupper()]) - sum([1 for c in extension if c.islower()])) for extension in extensions]
    strongest_extension = max(strengths, key = lambda x: x[1])
    return f"{class_name}.{strongest_extension[0]}"


