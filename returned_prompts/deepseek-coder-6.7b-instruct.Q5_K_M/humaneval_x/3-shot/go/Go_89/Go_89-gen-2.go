    shift := 2 * 2
    alphabet := "abcdefghijklmnopqrstuvwxyz"
    cipher := strings.Repeat(alphabet, 2)
    encrypted := ""

    for _, c := range s {
        if string(c) == " " {
            encrypted += " "
        } else {
            oldIndex := strings.Index(alphabet, strings.ToLower(string(c)))
            newIndex := (oldIndex + shift) % len(alphabet)
            if unicode.IsUpper(c) {
                encrypted += strings.ToUpper(string(cipher[newIndex]))
            } else {
                encrypted += string(cipher[newIndex])
            }
        }
    }
    return encrypted
}



