def reverse_vowels(s):
    vowels = "aeiou"
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] in vowels:
            if i < len(s_list) - 1 and s_list[i+1] in vowels:
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
    return "".join(s_list)