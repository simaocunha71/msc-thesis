def number_of_substrings(s):
    n = len(s)
    return n * (n + 1) // 2

assert number_of_substrings("abc") == 6
assert number_of_substrings("abcd") == 10
assert number_of_substrings("abcde") == 15
assert number_of_substrings("abcdef") == 21
assert number_of_substrings("abcdefg") == 28
assert number_of_substrings("abcdefgh") == 36
assert number_of_substrings("abcdefghi") == 45
assert number_of_substrings("abcdefghij") == 55
assert number_of_substrings("abcdefghijk") == 66
assert number_of_substrings("abcdefghijkl") == 78
assert number_of_substrings("abcdefghijklm") == 91
assert number_of_substrings("abcdefghijklmn") == 105
assert number_of_substrings("abcdefghijklmno") == 120
assert number_of_substrings("abcdefghijklmnop") == 136
assert number_of_substrings("abcdefghijklmnopq") == 153
assert number_of_substrings("abcdefghijklmnopqr") == 171
assert number_of_substrings("abcdefghijklmnopqrs") == 190
assert number_of_substrings("abcdefghijklmnopqrst") == 210
assert number_of_substrings("abcdefghijklmnopqrstu") == 231
assert number_of_substrings("abcdefghijklmnopqrstuv") == 253
assert number_of_substrings("abcdefghijklmnopqrstuvw") == 276
assert number_of_substrings("abcdefghijklmnopqrstuvwx") == 300
assert number_of_substrings("abcdefghijklmnopqrstuvwxy") == 325
assert number_of_substrings("abcdefghijklmnopqr