    shift := 2 * 2
    upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower := "abcdefghijklmnopqrstuvwxyz"
    encrypted := ""

    for _, c := range s {
        if strings.ContainsRune(upper, c) {
            pos := strings.Index(upper, string(c))
            newPos := (pos + shift) % len(upper)
            encrypted += string(upper[newPos])
        } else if strings.ContainsRune(lower, c) {
            pos := strings.Index(lower, string(c))
            newPos := (pos + shift) % len(lower)
            encrypted += string(lower[newPos])
        } else {
            encrypted += string(c)
        }
    }

    return encrypted
}



