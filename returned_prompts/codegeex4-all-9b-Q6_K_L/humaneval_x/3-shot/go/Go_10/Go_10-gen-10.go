    runes := []rune(str)
    for i := len(runes) - 1; i >= 0; i-- {
        if IsPalindrome(string(runes[i:])) {
            return str + string(runes[:i])
        }
    }
    return str
}

