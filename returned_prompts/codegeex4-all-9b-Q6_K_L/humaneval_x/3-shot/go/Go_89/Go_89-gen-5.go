    alphabet := "abcdefghijklmnopqrstuvwxyz"
    encrypted_s := ""

    for _, c := range s {
        index := strings.Index(alphabet, string(c))
        encrypted_c := alphabet[(index+4)%26]
        encrypted_s += string(encrypted_c)
    }
    return encrypted_s
}



