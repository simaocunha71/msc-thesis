    if IsPalindrome(str) {
        return str
    }

    for i := len(str); i >= 0; i-- {
        if IsPalindrome(str[:i]) {
            return str[:i] + strings.Repeat(str[i:i+1], 2)
        }
    }
    return ""
}



