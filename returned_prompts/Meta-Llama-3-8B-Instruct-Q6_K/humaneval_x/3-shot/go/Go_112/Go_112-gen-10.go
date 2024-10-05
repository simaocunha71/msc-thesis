    var result []byte
    for _, c1 := range s {
        if !strings.Contains(c, string(c1)) {
            result = append(result, c1)
        }
    }
    resultStr := string(result)
    return [2]interface{}{resultStr, strings.EqualFold(resultStr, reverse(resultStr))}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}