    cap_count = 0
    sm_count = 0
    strongest_extension = None
    for extension in extensions:
        cap_count = 0
        sm_count = 0
        for c in extension:
            if c.isupper():
                cap_count += 1
            elif c.islower():
                sm_count += 1
        strength = cap_count - sm_count
        if strength > 0 and (strongest_extension is None or strength > strongest_extension[1]):
            strongest_extension = (class_name, extension)
    return class_name + "." + strongest_extension[1]


