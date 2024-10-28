def string_to_list(s):
    return s.split()  # return a list of strings split on the space character
assert string_to_list("python programming")==['python','programming']
print(string_to_list("python programming"))  # Output: ['python', 'programming']  # test the function
# test the function
print(string_to_list("hello world"))  # Output: ['hello', 'world']  # test the function
print(string_to_list("   hello world  "))  # Output: ['hello', 'world']  # test the function
print(string_to_list("hello"))  # Output: ['hello']  # test the function
print(string_to_list(""))  # Output: []  # test the function
# test the function
print(string_to_list("   "))  # Output: []  # test the function
print(string_to_list("   a  b  "))  # Output: ['a', 'b']  # test the function
# test the function
print(string_to_list("  a  "))  # Output: ['a']  # test the function
print(string_to_list("   a  b  c"))  # Output: ['a', 'b', 'c']  # test the function
# test the function
print(string_to_list("a b c d"))  # Output: ['a', 'b', 'c', 'd']  # test the function
print(string_to_list("a  b c d"))  # Output: ['a', 'b', 'c', 'd']  # test the function
print(string_to_list("a b   c d"))  # Output: ['a', 'b', 'c', 'd']  # test the function
print(string_to_list("a b c   d"))  # Output: ['a', 'b', 'c', 'd']  # test the function
print(string_to_list("a b c d   "))  # Output: ['a', 'b', 'c', 'd']  # test the function
print(string_to_list("a b c d e"))  # Output: ['a', 'b', 'c', 'd', 'e']  # test the function
print(string_to_list("a b c d e f"))  # Output: ['a', 'b', 'c', 'd', 'e', 'f']  # test the function
print(string_to_list("a b