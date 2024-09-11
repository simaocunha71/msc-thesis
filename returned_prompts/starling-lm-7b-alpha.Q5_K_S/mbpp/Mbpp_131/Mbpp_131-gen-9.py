"""
def reverse_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    index = 0
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in vowel_list:
            s_list[i], s_list[index] = s_list[index], s_list[i]
            index += 1
    return ''.join(s_list)
"""

def reverse_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    index = 0
    s_list = list(s)
    n = len(s)
    for i in range(n):
        if s_list[i] in vowel_list:
            while s_list[index] not in vowel_list:
                index += 1
            s_list[i], s_list[index] = s_list[index], s_list[i]
            index += 1
    return ''.join(s_list)

def test(s):
    print(reverse_vowels(s))

test("Python")
test("Hello")
test("leetcode")
test("aA")
test("abcd")



"""
def reverse_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_list = list(s)
    start, end = 0, len(s) - 1
    while start < end:
        while s_list[start] not in vowel_list:
            start += 1
        while s_list[end] not in vowel_list:
            end -= 1
        if s_list[start] == s_list[end]:
            start += 1
            end -= 1
        else:
            s_list[start], s_list[end] = s_list[end], s