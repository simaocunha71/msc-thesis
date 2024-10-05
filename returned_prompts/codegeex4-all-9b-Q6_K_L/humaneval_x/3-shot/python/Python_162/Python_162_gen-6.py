    import hashlib

    if not text:
        return None

    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()

