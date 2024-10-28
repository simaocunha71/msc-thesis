    vowels := "aeiou"
    encoded := ""

    for _, c := range message {
        char := string(c)

        if strings.ContainsRune(vowels, c) {
            switch char {
            case "a":
                encoded += "c"
            case "e":
                encoded += "g"
            case "i":
                encoded += "k"
            case "o":
                encoded += "q"
            case "u":
                encoded += "w"
            default:
                encoded += char
            }
        } else {
            switch char {
            case "A":
                encoded += "C"
            case "E":
                encoded += "G"
            case "I":
                encoded += "K"
            case "O":
                encoded += "Q"
            case "U":
                encoded += "W"
            default:
                encoded += char
            }
        }
    }
    return encoded
}



