    if len(str) == 0 {
        return str
    }
    if IsPalindrome(str) {
        return str
    }
    for len(str) > 0 {
        suffix := str[len(str)-1:]
        if IsPalindrome(suffix) {
            prefix := str[:len(str)-len(suffix)]
            return prefix + suffix + string(reverse(prefix))
        }
        str = str[:len(str)-1]
    }
    return ""
}



