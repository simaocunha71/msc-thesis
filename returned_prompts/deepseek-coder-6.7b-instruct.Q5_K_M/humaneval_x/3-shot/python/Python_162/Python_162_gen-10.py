    import hashlib
    if text:
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    return None


