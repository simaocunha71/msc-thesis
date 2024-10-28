    result := strings.Replace(s, c, "", -1)
    return [2]interface{}{result, strings.Compare(result, reverse(result)) == 0}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

