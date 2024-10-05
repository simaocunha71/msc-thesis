    result := []rune{}
    for _, c := range s {
        if !strings.Contains(c, string(c)) {
            result = append(result, c)
        }
    }
    return [2]interface{}{string(result), strings.EqualFold(string(result), reverse(string(result)))}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}