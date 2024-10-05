    CAP_weight = lambda s: len([c for c in s if c.isupper()])
    SM_weight = lambda s: len([c for c in s if c.islower()])

    strongest_extension = extensions[0]
    strongest_weight = CAP_weight(strongest_extension) - SM_weight(strongest_extension)

    for ext in extensions[1:]:
        curr_weight = CAP_weight(ext) - SM_weight(ext)
        if curr_weight > strongest_weight:
            strongest_extension = ext
            strongest_weight = curr_weight

    return f"{class_name}.{strongest_extension}"


