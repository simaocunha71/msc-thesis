    import hashlib

    if not text:
        return None

    hash_md5 = hashlib.md5(text.encode())
    return hash_md5.hexdigest()  # Return the hexadecimal representation of the hash


