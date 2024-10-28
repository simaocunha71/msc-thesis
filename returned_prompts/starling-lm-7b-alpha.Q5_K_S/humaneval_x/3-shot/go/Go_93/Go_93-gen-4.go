    result := make([]rune, len(message))
    for i, c := range message {
        if c == 'a' {
            result[i] = 'c'
        }else if c == 'e' {
            result[i] = 'g'
        }else if c == 'i' {
            result[i] = 'k'
        }else if c == 'o' {
            result[i] = 'q'
        }else if c == 'u' {
            result[i] = 'w'
        }else {
            result[i] = (c + 'A' - 'a') % 26 + 'a'
        }
    }
    return string(result)
}



