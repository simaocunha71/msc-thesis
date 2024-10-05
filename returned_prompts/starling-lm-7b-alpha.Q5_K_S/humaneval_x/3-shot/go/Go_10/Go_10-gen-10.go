    if IsPalindrome(str) {
        return str
    }

    for suffix_len := len(str) / 2; suffix_len >= 1; suffix_len-- {
        if IsPalindrome(str[:suffix_len]) {
            return str[:suffix_len] + string(reverse(str[suffix_len:])) + string(reverse(str[:suffix_len]))
        }
    }
    return ""
}



