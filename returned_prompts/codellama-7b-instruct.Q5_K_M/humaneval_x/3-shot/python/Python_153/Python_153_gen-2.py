    extensions = sorted(extensions, key=lambda x: x.lower().count('a') - x.lower().count('b'))
    return f'{class_name}.{extensions[-1]}'


