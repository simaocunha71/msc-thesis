    class_name, extensions = class_name.lower(), [e.lower() for e in extensions]
    strongest_extension = extensions[0]
    strength = 0
    for ext in extensions:
        cap_count = sum(1 for c in ext if c.isupper())
        sm_count = sum(1 for c in ext if c.islower())
        curr_strength = cap_count - sm_count
        if curr_strength > strength:
            strength = curr_strength
            strongest_extension = ext

    return ".".join([class_name] + [strongest_extension])


