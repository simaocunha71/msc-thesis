def reverse_vowels(s):
    vowels = "aeiou"
    i, j = 0, len(s)-1
    s = list(s)
    while i < j:
        while s[i] not in vowels:
            i += 1
        while s[j] not in vowels:
            j -= 1
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return "".join(s)

# assert reverse_vowels("Python") == "Python"

def reverse_vowels_2(s):
    vowel_set = set("aeiou")
    s_list = list(s)
    for i, char in enumerate(s_list):
        if char in vowel_set:
            j = len(s_list)-1-i
            s_list[i], s_list[j] = s_list[j], s_list[i]
    return "".join(s_list)

def reverse_vowels_3(s):
    vowel_set = set("aeiou")
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in vowel_set:
            j = len(s_list)-1-i
            s_list[i], s_list[j] = s_list[j], s_list[i]
    return "".join(s_list)

# assert reverse_vowels_2("Python") == "Python"
# assert reverse_vowels_3("Python") == "Python"


"""
Python的字符串是不可变的，所以不能直接交换字符串中的两个字符。
如果我们想要交换两个字符串中的某个字符，我们需要将其转换为列表，再进行交换，最后再将其转换回字符串。
"""

def reverse_vowels_4