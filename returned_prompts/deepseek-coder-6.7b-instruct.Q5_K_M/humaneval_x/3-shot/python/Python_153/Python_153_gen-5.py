    strongest_ext = max(extensions, key=lambda ext: sum(c.isupper() for c in ext) - sum(c.islower() for c in ext))
    return f"{class_name}.{strongest_ext}"


