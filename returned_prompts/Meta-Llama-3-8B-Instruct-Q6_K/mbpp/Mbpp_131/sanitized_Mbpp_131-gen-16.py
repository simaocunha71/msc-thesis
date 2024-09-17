def reverse_vowels(s):
    vowels = "aeiouAEIOU"
    s_list = list(s)
    left, right = 0, len(s_list) - 1
    while left < right:
        if s_list[left] not in vowels:
            left += 1
        elif s_list[right] not in vowels:
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left, right = left + 1, right - 1
    return "".join(s_list)  # or return "".join(s_list) if you want to keep the original string