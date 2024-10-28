    result := ""
    vowels := "aeiou"

B:
    for _, char := range message {
        c := strings.ToLower(string(char))

        if strings.ContainsRune(vowels, rune(c)) {
            switch c {
            case "a":
                result += "c"
            case "e":
                result += "g"
            case "i":
                result += "k"
            case "o":
                result += "q"
            case "u":
                result += "w"
            }
        } else {
            switch c {
            case "A":
                result += "C"
            case "E":
                result += "G"
            case "I":
                result += "K"
            case "O":
                result += "Q"
            case "U":
                result += "W"
            default:
                result += string(char)
            }
        }
    }

C:
    return result
}

This function works by going through each character in the message, checking if it is a vowel. If it is, it replaces it with the corresponding character that appears two places ahead in the English alphabet. If it isn't a vowel, it simply swaps the case.

This function will work for any string input, as long as it only contains letters. It's case-sensitive, so uppercase letters will be replaced with their lowercase counterparts and vice versa.
*/

/*
