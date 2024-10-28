    import hashlib

    md5_hash = hashlib.md5(text.encode('utf-8'))
    return md5_hash.hexdigest() if text else None


