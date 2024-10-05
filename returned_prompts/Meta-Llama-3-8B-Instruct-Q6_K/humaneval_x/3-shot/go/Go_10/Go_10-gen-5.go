    runes := []rune(str)
    i := 0
    while i < len(runes) && runes[i] == runes[len(runes)-1-i] {
        i++
    }
    return string(runes[:i]) + string(rune(reverse(runes[i:])))
}

func reverse(s []rune) []rune {
    result := make([]rune, 0)
    for i := len(s) - 1; i >= 0; i-- {
        result = append(result, s[i])
    }
    return result
}