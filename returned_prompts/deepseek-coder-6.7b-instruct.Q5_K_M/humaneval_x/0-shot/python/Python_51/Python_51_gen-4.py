
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join([char for char in text if char not in vowels])



if __name__ == "__main__":
    import doctest
    doctest.testmod()

#tests/test_remove_vowels.py
import pytest
from remove_vowels import remove_vowels

def test_empty_string():
    assert remove_vowels('') == ''

def test_all_vowels():
    assert remove_vowels('aeiou') == ''

def test_mixed_case_vowels():
    assert remove_vowels('aeiOU') == ''

def test_no_vowels():
    assert remove_vowels('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ') == 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

def test_random_words():
    assert remove_vowels('abcdefghijklmnopqrstuvwxyz') == 'bcdfghjklmnpqrstvwxyz'

def test_random_words_with_vowels():
    assert remove_vowels('aaaeeeiiiioooouuu') == ''

def test_random_words_with_mixed_case_vowels():
    assert remove_vowels('AbCdeFgHiJkLmNoPqRsTuVwXyZ') == 'bcdfghjklmnpqrstvwxyz'

def test_random_words_with_new_line():
    assert remove_vowels('abc\ndef\nghi\njkl\nmn\nopq\nrst\nvw\nxyz') == 'bcd\nfgh\njkl\nmn\nopq\nrst\nvw\