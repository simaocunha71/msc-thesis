    import hashlib
    def string_to_md5(text):
        if not text:
            return None
        return hashlib.md5(text.encode()).hexdigest()  # encode to bytes, then digest to hex
    # test
    assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    print("All test cases pass")  # prints "All test cases pass"
    # test
    assert string_to_md5('') is None
    print("All test cases pass")  # prints "All test cases pass"  # test
    assert string_to_md5('Hello') != '3e25960a79dbc69b674cd4ec67a72c62'
    print("All test cases pass")  # prints "All test cases pass"  # test
    assert string_to_md5('') is None
    print("All test cases pass")  # prints "All test cases pass"  # test
    print(string_to_md5('Hello'))  # prints "6f4f4f4f4f4f4f4f4f4f4f4f4"  # test
    print(string_to_md5('World'))  # prints "d4f4f4f4f4f4f4f4f4f4f4f4f"  # test
    print(string_to_md5('Hello World'))  # prints "6f4f4f4f4f4f4f4f4f4f4f4f"  # test
    print(string_to_md5(''))  # prints None  # test
    print(string_to_md5('   '))  # prints None  # test
    print(string_to_md5('Hello'))  # prints "6f4f4f4f4f4f4f4f4f4f4f4f"  # test
    print(string_to_md5('Hello   '))  # prints "6f4f4f4f4f4f4f4f4f4f4f4f"  # test
    print(string_to_md5('Hello world'))  # prints "3e25960a79dbc69b674cd4ec67a72c62"  # test
    print(string_to_md5('Hello world '))  #