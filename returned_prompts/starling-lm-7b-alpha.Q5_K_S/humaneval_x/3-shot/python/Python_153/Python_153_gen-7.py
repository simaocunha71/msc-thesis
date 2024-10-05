    cap_count = sum(1 for c in extensions if c.isupper())
    small_count = sum(1 for c in extensions if c.islower())
    strength = cap_count - small_count

    best_ext = extensions[0]
    for ext in extensions[1:]:
        if strength(ext) != strength(best_ext):
            if strength(ext) > strength(best_ext):
                best_ext = ext
        elif strength(ext) == strength(best_ext):
            if extensions.index(ext) < extensions.index(best_ext):
                best_ext = ext

    return f"{class_name}.{best_ext}"


