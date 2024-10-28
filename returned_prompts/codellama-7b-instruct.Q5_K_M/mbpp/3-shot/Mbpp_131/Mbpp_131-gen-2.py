
def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    s_list = list(s)
    for i in range(len(s)):
        if s_list[i] in vowels:
            s_list[i] = s[-i - 1]
    return ''.join(s_list)


