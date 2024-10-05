    shift := 2 * 2
    upper := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower := "abcdefghijklmnopqrstuvwxyz"
    upper_rot := strings.Repeat(upper, 2)[shift:len(s)+shift]
    lower_rot := strings.Repeat(lower, 2)[shift:len(s)+shift]
    encrypted := ""

    for _, c := range s {
        if strings.ContainsRune(upper, c) {
            encrypted += string(upper_rot[strings.IndexRune(upper, c)])
        } else if strings.ContainsRune(lower, c) {
            encrypted += string(lower_rot[strings.IndexRune(lower, c)])
        } else {
            encrypted += string(c)
        }
    }

    return encrypted
}



