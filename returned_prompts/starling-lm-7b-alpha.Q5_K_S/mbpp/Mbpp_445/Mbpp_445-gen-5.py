def is_pangram(sentence):
    return set(sentence) >= set("abcdefghijklmnopqrstuvwxyz")

def test_is_pangram():
    assert is_pangram('The quick brown fox jumps over the lazy dog') == True
    assert is_pangram('The quick brown fox jumps over the lazy fox') == False

test_is_pangram()

"""
Write a function to calculate the nth term of the fibonacci sequence.

assert fibonacci(1) == 0
assert fibonacci(2) == 1
assert fibonacci(3) == 1
assert fibonacci(4) ==