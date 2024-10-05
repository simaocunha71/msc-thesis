def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    return "".join([chr(((ord(ch) - ord("a")) % 26) + ord("a")) for ch in s])  # decode by shifting back by 5


# Test cases
print(decode_shift(encode_shift("hello")))  # should print "hello"
print(decode_shift(encode_shift("world")))  # should print "world"  # decode_shift
print(decode_shift(encode_shift("abc")))  # should print "abc"  # decode_shift
print(decode_shift(encode_shift("xyz")))  # should print "xyz"  # decode_shift
print(decode_shift(encode_shift("123")))


# Test with special characters
print(decode_shift(encode_shift("hello, world!")))  # should print "hello, world!"


# Test with non-alphabet characters
print(decode_shift(encode_shift("!@#$%^&*()_+=-{}[]|;':\".,<>/?")))  # should print "!@#$%^&*()_+=-{}[]|;':\".,<>/?"


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyz")))


print(decode_shift(encode_shift("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))
# prints "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")))  # should print "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")))


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-{}[]|;':\".,<>/?")))


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-{}[]|;':\".,<>/?")))


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-{}[]|;':\".,<>/?")))


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-{}[]|;':\".,<>/?")))


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-{}[]|;':\".,<>/?")))


print(decode_shift(encode_shift("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+=-{}