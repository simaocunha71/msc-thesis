    def string_to_md5(text):
        if not text: 
            return None
        import hashlib
        return hashlib.md5(text.encode()).hexdigest()  # convert to bytes first, then encode to bytes-like object
    # Test cases
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert string_to_md5('') is None
    assert string_to_md5('a') == 'a5bab5e45e5f5c5c'
    # Your test case here
    # assert string_to_md5('') == None
    # assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    # assert string_to_md5('1234567890') == 'd7a8f5c3e5d4d0b5'
    # assert string_to_md5('hello') == '5d41402abcce912c7a6ae2569b4c4f8f'

    # Your test case here
    # assert string_to_md5('') == None
    # assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    # assert string_to_md5('1234567890') == 'd7a8f5c3e5d4d0b5'
    # assert string_to_md5('hello') == '5d41402abcce912c7a6ae2569b4c4f8f'
    # assert string_to_md5('') == None
    # assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    # assert string_to_md5('1234567890') == 'd7a8f5c3e5d4d0b5'
    # assert string_to_md5('hello') == '5d41402abcce912c7a6ae2569b4c4f8f'
    # assert string_to_md5('') == None
    # assert string_to_md5('test') == '098f6bcd4621d373cade4e832627b4f6'
    # assert string_to_md5('1234567890') ==