    runes := []rune(str)
    result := []rune{}
    i := len(runes) - 1
    for i >= 0 {
        for j := i; j >= 0; j-- {
            if runes[j] == runes[i] {
                i--
                break
            }
        }
        result = append(result, runes[i])
        i--
    }
    for _, r := range runes[:len(runes)-i-1] {
        result = append([]rune{r}, result...)
    }
    return string(result)
} 