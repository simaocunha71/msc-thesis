    return f"{class_name}.{sorted(extensions, key=lambda x: x.lower().count('a') - x.lower().count('b'))[0]}"


