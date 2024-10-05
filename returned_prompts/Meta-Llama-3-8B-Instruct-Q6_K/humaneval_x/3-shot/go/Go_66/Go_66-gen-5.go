    sum := 0
    for _, c := range x {
        if unicode.IsUpper(rune(c)) {
            sum += int(c - 64)
        }
    }
    return sum
}