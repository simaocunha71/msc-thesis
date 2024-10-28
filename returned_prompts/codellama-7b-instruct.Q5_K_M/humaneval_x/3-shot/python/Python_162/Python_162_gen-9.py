    import hashlib
    import binascii

    if text == '':
        return None

    return binascii.hexlify(hashlib.md5(text.encode('utf-8')).digest()).decode('utf-8')


