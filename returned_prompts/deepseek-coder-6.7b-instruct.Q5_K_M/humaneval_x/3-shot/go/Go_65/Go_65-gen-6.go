    s := strconv.Itoa(x)
    length := len(s)

    if shift > length {
        return reverse(s)
    }

    return s[length-shift:] + s[:length-shift]
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}


