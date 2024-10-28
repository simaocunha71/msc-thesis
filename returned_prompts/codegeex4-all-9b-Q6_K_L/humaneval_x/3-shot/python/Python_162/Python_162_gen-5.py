    import hashlib

    if not text:
        return None

    m = hashlib.md5()
    m.update(text.encode('utf-8'))
    return m.hexdigest()

