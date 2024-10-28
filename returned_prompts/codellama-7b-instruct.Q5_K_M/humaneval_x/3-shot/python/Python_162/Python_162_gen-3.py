    import hashlib
    import binascii

    if text == '':
        return None

    hash = hashlib.md5()
    hash.update(text.encode('utf-8'))
    return binascii.hexlify(hash.digest()).decode('utf-8')


