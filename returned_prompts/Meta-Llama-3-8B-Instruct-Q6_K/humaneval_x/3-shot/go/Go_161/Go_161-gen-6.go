    result := ""
    for _, c := range s {
        if 'a' <= c && c <= 'z' {
            result += string('A' + c - 'a')
        } else if 'A' <= c && c <= 'Z' {
            result += string('a' + c - 'A')
        } else {
            result += string(c)
        }
    }
    if len(result) == 0 {
        return reverse(s)
    }
    return result
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
}