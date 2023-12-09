
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    # Create a hash object
    md5 = hashlib.md5() 

    # Add the string to hash
    md5.update(text)

    return md5.hexdigest().upper()
    
def string_to_sha1(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_sha1('Hello world') == '09b271c43eef94d8de654f570959fed0bc1cafc6'
    """
    
    # Create a hash object
    sha = hashlib.sha1() 
    
    # Add the string to hash
    sha.update(text)
    
    return sha.hexdigest().upper()