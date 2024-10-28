    cap_count = lambda x: sum(1 for c in x if c.isupper())
    lower_count = lambda x: sum(1 for c in x if c.islower())

    strengths = {x: cap_count(x) - lower_count(x) for x in extensions}
    max_strength = max(strengths.values())
    max_strength_extensions = [k for k, v in strengths.items() if v == max_strength]

    return class_name + '.' + max_strength_extensions[0]


