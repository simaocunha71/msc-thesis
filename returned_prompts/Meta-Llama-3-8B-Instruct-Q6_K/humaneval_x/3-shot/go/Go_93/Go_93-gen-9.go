    result := make([]byte, 0)
    for _, c := range message {
        if c >= 'a' && c <= 'z' {
            if c == 'a' {
                result = append(result, 'c')
            } else if c == 'e' {
                result = append(result, 'g')
            } else if c == 'i' {
                result = append(result, 'k')
            } else if c == 'o' {
                result = append(result, 'q')
            } else if c == 'u' {
                result = append(result, 'w')
            } else {
                result = append(result, byte(c) + 1)
            }
        } else if c >= 'A' && c <= 'Z' {
            if c == 'A' {
                result = append(result, 'C')
            } else if c == 'E' {
                result = append(result, 'G')
            } else if c == 'I' {
                result = append(result, 'K')
            } else if c == 'O' {
                result = append(result, 'Q')
            } else if c == 'U' {
                result = append(result, 'W')
            } else {
                result = append(result, byte(c) + 1)
            }
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}