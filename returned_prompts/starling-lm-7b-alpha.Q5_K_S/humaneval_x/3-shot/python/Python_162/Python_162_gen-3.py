    import hashlib

    if not text:
        return None

    return hashlib.md5(text.encode('utf-8')).hexdigest()


