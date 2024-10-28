    import hashlib
    import binascii
    if text == '':
        return None
    else:
        return binascii.hexlify(hashlib.md5(text.encode()).digest()).decode()


