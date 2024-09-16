def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            j = len(s) - i -1
            while j >= 0 and s_list[j] in vowels:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                j -= 1
    return "".join(s_list)