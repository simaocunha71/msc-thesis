    encoded = strings.ToUpper(message)
    for i := 0; i < len(encoded); i++ {
        c := encoded[i]
        switch c {
        case 'A':
            encoded = strings.Replace(encoded, "A", "C", -1)
        case 'E':
            encoded = strings.Replace(encoded, "E", "G", -1)
        case 'I':
            encoded = strings.Replace(encoded, "I", "K", -1)
        case 'O':
            encoded = strings.Replace(encoded, "O", "Q", -1)
        case 'U':
            encoded = strings.Replace(encoded, "U", "W", -1)
        }
    }
    return encoded
}

