    result := make([]rune, 0, len(message))
    for _, c := range message {
        if c >= 'a' && c <= 'z' {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                c += 2
            }
            c = (c + 'A' - 'a')
        }
        result = append(result, c)
    }
    return string(result)
}



