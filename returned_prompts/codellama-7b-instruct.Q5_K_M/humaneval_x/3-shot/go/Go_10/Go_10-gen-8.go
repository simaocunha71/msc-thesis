    if IsPalindrome(str) {
        return str
    }
    for i := len(str); i > 0; i-- {
        substr := str[:i]
        if IsPalindrome(substr) {
            return substr + strings.Repeat(str[i:], 2)
        }
    }
    return str + strings.Repeat(str, 2)
}



