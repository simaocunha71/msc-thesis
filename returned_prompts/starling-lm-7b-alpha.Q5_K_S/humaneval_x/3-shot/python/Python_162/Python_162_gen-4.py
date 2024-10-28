    import hashlib
    if len(text) == 0:
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


