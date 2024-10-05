    if IsPalindrome(str) {
        return str
    }

    var postfix string
    for i := 0; i < len(str); i++ {
        sub := str[i:]
        if IsPalindrome(sub) {
            postfix = sub
            break
        }
    }

    var prefix string
    for i := len(str) - 1; i >= 0; i-- {
        sub := str[:i]
        if IsPalindrome(sub) {
            prefix = sub
            break
        }
    }

    return str + prefix[len(prefix):]
}



