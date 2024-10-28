    import hashlib

    if text == '':
        return None

    return hashlib.md5(text.encode()).hexdigest()


