    s := strconv.Itoa(x)
    len := len(s)
    if shift >= len {
        return reverse(s)
    }
    return s[len-shift:] + s[:len-shift]
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



