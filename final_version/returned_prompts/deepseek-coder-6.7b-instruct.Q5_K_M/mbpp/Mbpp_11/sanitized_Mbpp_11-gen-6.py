def remove_Occ(s, c):
    # find the first and last occurrence of the character
    first_occurrence = s.find(c)
    last_occurrence = s.rfind(c)

    # remove the first and last occurrence
    if first_occurrence != -1 and last_occurrence != -1:
        s = s[:first_occurrence] + s[last_occurrence + 1:]
    return s