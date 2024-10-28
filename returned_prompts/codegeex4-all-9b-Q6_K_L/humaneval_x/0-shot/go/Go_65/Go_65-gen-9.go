func CircularShift(x int, shift int) string {
    s := strconv.Itoa(x)
    if shift > len(s) {
        return reverse(s)
    }
    shift %= len(s)
    return s[shift:] + s[:shift]
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
