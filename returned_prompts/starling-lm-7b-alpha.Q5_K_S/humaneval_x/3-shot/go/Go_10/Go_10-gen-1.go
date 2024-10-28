    var result string
    if IsPalindrome(str) {
        return str
    }
    pal := makePalindromeSuffix(str)
    for i := 0; i < len(str); i++ {
        candidate := str[i : len(str)-len(pal)] + string(reverse(str[0:i]))
        if IsPalindrome(candidate) {
            result = candidate
            break
        }
    }
    return result
}

func makePalindromeSuffix(str string) string {
    var result string
    for i := len(str) - 1; i >= 0; i-- {
        candidate := str[i : len(str)]
        if IsPalindrome(candidate) {
            result = candidate
            break
        }
    }
    return result
}

func reverse(str string) string {
    return string(reverseRune(str))
}

func reverseRune(str string) []rune {
    result := make([]rune, 0)
    for _, r := range str {
        result = append([]rune{r}, result...)
    }
    return result
}



