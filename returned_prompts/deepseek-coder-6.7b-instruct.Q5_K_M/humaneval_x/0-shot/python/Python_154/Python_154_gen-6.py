
    # Python program to implement
    # the above approach

    def cycpattern_check(a, b):
        # concatenate a with itself
        temp = a + a

        # check if b is substring of temp
        if b in temp:
            return True
        else:
            return False


    # Driver code
    a = "himenss"
    b = "simen"
    print(cycpattern_check(a, b))

    a = "abcd"
    b = "abd"
    print(cycpattern_check(a, b))

    a = "hello"
    b = "ell"
    print(cycpattern_check(a, b))

    a = "whassup"
    b = "psus"
    print(cycpattern_check(a, b))

    a = "abab"
    b = "baa"
    print(cycpattern_check(a, b))

    a = "efef"
    b = "eeff"
    print(cycpattern_check(a, b))

    # This code is contributed
    # by Code_Mech
    # Python program to implement
    # the above approach

    def cycpattern_check(a, b):
        # concatenate a with itself
        temp = a + a

        # check if b is substring of temp
        if b in temp:
            return True
        else:
            return False


    # Driver code
    a = "himenss"
    b = "simen"
    print(cycpattern_check(a, b))

    a = "abcd"
    b = "abd"
    print(cycpattern_check(a, b))

    a = "hello"
    b = "ell"
    print(cycpattern_check(a, b))

    a = "whassup"
    b = "psus"
    print(cycpattern_check(a, b))

    a = "abab"
    b = "baa"
    print(cycpattern_check(a