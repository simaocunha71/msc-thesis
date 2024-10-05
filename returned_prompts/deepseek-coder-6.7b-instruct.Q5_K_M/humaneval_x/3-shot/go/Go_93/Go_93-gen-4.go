    vowels := []string{"a", "e", "i", "o", "u"}
    encoded := ""
    for _, c := range message {
        char := strings.ToLower(string(c))
        if strings.Contains(char, vowels[0]) {
            encoded += "e"
        }else if strings.Contains(char, vowels[1]) {
            encoded += "i"
        }else if strings.Contains(char, vowels[2]) {
            encoded += "o"
        }else if strings.Contains(char, vowels[3]) {
            encoded += "u"
        }else if strings.Contains(char, vowels[4]) {
            encoded += "a"
        }else if c >= 'A' && c <= 'Z' {
            encoded += strings.ToLower(string(c))
        }else if c >= 'a' && c <= 'z' {
            encoded += strings.ToUpper(string(c))
        }else {
            encoded += string(c)
        }
    }
    return encoded
}



