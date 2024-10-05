    result := make([]rune, 0)
    for _, c := range message {
        if (c >= 'a' && c <= 'z') {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
                c += 2
                if c > 'z' {
                    c -= 26
                }
            } else {
                c ^= 'a' ^ 'A'
            }
        }
        result = append(result, c)
    }
    return string(result)
}



