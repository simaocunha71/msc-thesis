
    import hashlib

    if not text:
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()
