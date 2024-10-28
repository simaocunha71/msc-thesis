    strongest_extension = max(extensions, key=lambda extension: sum(1 for c in extension if c.isupper) - sum(1 for c in extension if c.islower))
    return f"{class_name}.{strongest_extension}"


