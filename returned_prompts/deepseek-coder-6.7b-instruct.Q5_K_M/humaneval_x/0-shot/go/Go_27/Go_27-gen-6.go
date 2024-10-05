    flipped := ""

B:
    for _, char := range str {
        if unicode.IsLower(char) {
            flipped += strings.ToUpper(string(char))
        } else {
            flipped += strings.ToLower(string(char))
        }
    }

    return flipped
}

