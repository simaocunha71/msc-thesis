
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in s:
        if letter in vowels or (letter == 'y' and letter == s[-1]):
            count += 1
    return count


def test_vowels_count(vowels_count, expected, s):
    result = vowels_count(s)
    assert result == expected, 'vowels_count({!r}) returned {!r}, expected {!r}'.format(s, result, expected)


if __name__ == '__main__':
    test_vowels_count(vowels_count, 2, 'abcde')
    test_vowels_count(vowels_count, 3, 'ACEDY')
    test_vowels_count(vowels_count, 0, 'abcd')
    test_vowels_count(vowels_count, 1, 'aeiou')
    test_vowels_count(vowels_count, 4, 'aeiouAEIOU')
    test_vowels_count(vowels_count, 3, 'aeiouAEIOUy')
    test_vowels_count(vowels_count, 4, 'aeiouAEIOUyY')
    test_vowels_count(vowels_count, 0, 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')

    print('OK')
