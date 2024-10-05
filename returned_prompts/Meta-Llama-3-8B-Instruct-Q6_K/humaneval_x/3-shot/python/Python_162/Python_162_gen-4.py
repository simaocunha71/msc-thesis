    import hashlib

    if not text:
        return None
    md5_hash = hashlib.md5(text.encode())
    return md5_hash.hexdigest()  # Return the hash as a hexadecimal string


