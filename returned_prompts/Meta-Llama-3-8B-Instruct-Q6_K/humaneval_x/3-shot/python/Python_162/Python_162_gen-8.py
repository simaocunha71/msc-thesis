    import hashlib
    if not text:
        return None
    return hashlib.md5(text.encode()).hexdigest()  # encode is used to convert string to bytes


