
def vowels_count(s):
    vowels = 0
    for i in s:
        if i in "aeiouy":
            vowels += 1
    return vowels

TESTS = [
    ("abcde", 2),
    ("ACEDY", 3),
    ("aeiouy", 6),
    ("bcdfghjklmnpqrstvwxz", 0),
    ("abcdABCD", 2),
    ("aeiouAEIOU", 6),
    ("yY", 1),
    ("aeiouAEIOUyY", 7),
]

def verify(actual, expected):
    assert actual == expected, f"{actual!r} != {expected!r}"

for test, expected in TESTS:
    verify(vowels_count(test), expected)
