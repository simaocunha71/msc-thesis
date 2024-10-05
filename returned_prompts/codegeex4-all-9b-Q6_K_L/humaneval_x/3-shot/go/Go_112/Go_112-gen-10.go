    result := ""
    for _, s_c := range s{
        if strings.IndexRune(c,s_c) == -1{
            result += string(s_c)
        }
    }
    return [2]interface{}{result, result == reverse(result)}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

