    return "".join([chr(((ord(ch) - 5 + ord("a")) % 26) + ord("a")) for ch in s])


# test

print(encode_shift("abc"))  # Output: "fgh"
print(decode_shift("fgh"))  # Output: "abc"


# test edge cases

print(encode_shift(""))  # Output: ""
print(decode_shift(""))  # Output: ""
print(encode_shift("z"))  # Output: "c"
print(decode_shift("c"))  # Output: "z"
print(encode_shift("zabc"))  # Output: "cdef"
print(decode_shift("cdef"))  # Output: "zabc"
print(encode_shift("abcdefghijklmnopqrstuvwxyz"))  # Output: "fghijklmnopqrstuvwxyza"
print(decode_shift("fghijklmnopqrstuvwxyza"))  # Output: "abcdefghijklmnopqrstuvwxyz"
print(encode_shift("abcdefghijklmnopqrstuvwxyza"))  # Output: "jklmnopqrstuvwxyzabcfed"
print(decode_shift("jklmnopqrstuvwxyzabcfed"))  # Output: "abcdefghijklmnopqrstuvwxyza"


# test invalid inputs

print(encode_shift(123))  # Output: Traceback (most recent call last): ...
print(decode_shift(123))  # Output: Traceback (most recent call last): ...
print(encode_shift("abc "))  # Output: Traceback (most recent call last): ...
print(decode_shift("abc "))  # Output: Traceback (most recent call last): ...
print(encode_shift("ab1c"))  # Output: Traceback (most recent call last): ...
print(decode_shift("ab1c"))  # Output: Traceback (most recent call last): ...


# test special cases

print(encode_shift("@"))  #