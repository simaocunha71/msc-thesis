    runes := []rune(str)
    for i := len(runes) - 1; i >= 0; i-- {
        if IsPalindrome(string(runes[i:])) {
            return str + string(Reverse(runes[:i]))
        }
    }
    return str
}
func Reverse(runes []rune) []rune {
    result := make([]rune, len(runes))
    for i, j := len(runes)-1, 0; i >= 0; i, j = i-1, j+1 {
        result[j] = runes[i]
    }
    return result
}

