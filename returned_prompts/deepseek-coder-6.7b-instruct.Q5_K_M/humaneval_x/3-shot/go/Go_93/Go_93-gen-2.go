    vowels := "aeiouAEIOU"
    encoded := ""
    for _, c := range message {
        if strings.ContainsRune(vowels, c) {
            switch c {
            case 'a', 'A':
                encoded += "C"
            case 'e', 'E':
                encoded += "G"
            case 'i', 'I':
                encoded += "K"
            case 'o', 'O':
                encoded += "Q"
            case 'u', 'U':
                encoded += "W"
            }
        } else {
            encoded += strings.ToUpper(string(c))
        }
    }
    return encoded
}



