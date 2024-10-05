    if not text:
        return None

    return md5(text.encode()).hexdigest()


