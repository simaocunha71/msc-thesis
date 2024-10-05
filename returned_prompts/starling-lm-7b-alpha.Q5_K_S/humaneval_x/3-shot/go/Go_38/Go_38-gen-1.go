    result := make([]rune, 0)
    for i := 0; i < len(s); i += 3 {
        char := rune(s[i])
        if i+2 < len(s) {
            char += rune(s[i+2])
            char -= rune(s[i+1])
        }
        result = append(result, char)
    }
    return string(result)
}



