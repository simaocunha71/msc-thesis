    import hashlib
    return hashlib.md5(text.encode("utf-8")).hexdigest() if text else None


