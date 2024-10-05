    shift := 2 * 2
    upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower := "abcdefghijklmnopqrstuvwxyz"
    encrypted := ""

    for _, c := range s {
        if strings.ContainsRune(upper, c) {
            newIndex := (int(c-'A') + shift) % len(upper)
            encrypted += string(upper[newIndex])
        } else if strings.ContainsRune(lower, c) {
            newIndex := (int(c-'a') + shift) % len(lower)
            encrypted += string(lower[newIndex])
        } else {
            encrypted += string(c)
        }
    }
    return encrypted
}



