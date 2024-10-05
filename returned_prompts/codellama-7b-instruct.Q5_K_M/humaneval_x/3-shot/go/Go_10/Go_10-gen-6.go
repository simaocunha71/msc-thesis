    if IsPalindrome(str) {
        return str
    }

    if len(str) == 1 {
        return str + str
    }

    for i := len(str) - 1; i >= 0; i-- {
        if IsPalindrome(str[:i+1]) {
            return str[:i+1] + strings.Reverse(str[:i])
        }
    }

    return str + strings.Reverse(str)
}



