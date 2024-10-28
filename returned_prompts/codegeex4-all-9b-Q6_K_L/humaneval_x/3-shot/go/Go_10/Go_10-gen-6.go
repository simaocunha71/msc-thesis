    runes := []rune(str)
    for i := len(runes); i > 0; i-- {
        if IsPalindrome(string(runes[:i])) {
            return str + string(reverse(runes[i:]))
        }
    }
    return str
}

func reverse(str []rune) []rune {
    result := make([]rune, len(str))
    for i, j := len(str)-1, 0; i >= 0; i, j = i-1, j+1 {
        result[j] = str[i]
    }
    return result
}

