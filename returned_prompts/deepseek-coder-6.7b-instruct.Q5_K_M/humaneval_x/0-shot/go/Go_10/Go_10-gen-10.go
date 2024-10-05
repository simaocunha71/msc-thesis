    for i := len(str) - 1; i >= 0; i-- {
        if IsPalindrome(str[:i+1]) {
            return str + reverse(str[i+1:])
        }
    }
    return str + reverse(str)