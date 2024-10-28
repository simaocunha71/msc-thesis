    if !IsPalindrome(str) {
        for i := len(str) - 1; i >= 0; i-- {
            prefix := str[:i]
            suffix := str[i:]
            if IsPalindrome(suffix) {
                return suffix + prefix
            }
        }
    }
    return str
}



