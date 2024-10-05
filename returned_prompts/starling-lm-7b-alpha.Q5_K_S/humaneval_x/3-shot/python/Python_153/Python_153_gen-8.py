    cap_count = 0
    sm_count = 0
    strongest_strength = -1
    strongest_extension = ""
    for extension in extensions:
        cap_count = len([c for c in extension if c.isupper()])
        sm_count = len([c for c in extension if c.islower()])
        strength = cap_count - sm_count
        if strength >= strongest_strength:
            strongest_strength = strength
            strongest_extension = extension
    return class_name + "." + strongest_extension


