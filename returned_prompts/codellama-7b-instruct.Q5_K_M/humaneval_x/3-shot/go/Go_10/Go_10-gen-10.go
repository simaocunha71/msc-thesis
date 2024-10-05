    if IsPalindrome(str) {
        return str
    }

    var prefix string
    for i := 0; i < len(str); i++ {
        if IsPalindrome(str[i:]) {
            prefix = str[:i]
            break
        }
    }
    return prefix + strings.Reverse(prefix)
}



