def reverse_vowels(s):
    vowel_list = ['a', 'e', 'i', 'o', 'u']
    index = 0
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in vowel_list:
            s_list[i], s_list[index] = s_list[index], s_list[i]
            index += 1
    return ''.join(s_list)