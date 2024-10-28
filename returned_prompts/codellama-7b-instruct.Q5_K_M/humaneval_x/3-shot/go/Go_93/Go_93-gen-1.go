    result := make([]rune, 0)
    for _, c := range message {
        if c>='a' && c<='z' {
            result = append(result, rune(65+c-97))
        } else if c>='A' && c<='Z' {
            result = append(result, rune(97+c-65))
        } else if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' {
            result = append(result, rune(c+2))
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}



