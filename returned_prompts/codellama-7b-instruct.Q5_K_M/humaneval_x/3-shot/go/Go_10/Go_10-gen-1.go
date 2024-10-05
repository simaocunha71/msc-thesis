    if IsPalindrome(str) {
        return str
    }
    for i := len(str) - 1; i >= 0; i-- {
        if IsPalindrome(str[0:i] + str[i+1:]) {
            return str[0:i] + strings.Repeat(str[i], (len(str) - i) / 2)
        }
    }
    return str
}



