def first_non_repeating_character(s):
    char_list = []
    for i in range(len(s)):
        if s.count(s[i]) == 1:
            char_list.append(s[i])
    if len(char_list) == 0:
        return None
    else:
        return char_list[0]