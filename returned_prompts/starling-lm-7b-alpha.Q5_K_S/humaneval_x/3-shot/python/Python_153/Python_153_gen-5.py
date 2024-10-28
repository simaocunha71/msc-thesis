    class_name, extensions = class_name.lower(), extensions
    strengths = [(sum(1 for c in ext if c.isupper()) - sum(1 for c in ext if c.islower()), idx)
                 for idx, ext in enumerate(extensions)]
    _, idx = max(strengths)
    return '{}.{}'.format(class_name, extensions[idx])


