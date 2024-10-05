    s2 := strings.Map(func(r rune) rune {
        if strings.ContainsRune(c, r) {
            return -1
        }
        return r
    }, s)

    s3 := strings.ReplaceAll(s2, string(-1), "")

    return [2]interface{}{s3, s3 == reverse(s3)}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



