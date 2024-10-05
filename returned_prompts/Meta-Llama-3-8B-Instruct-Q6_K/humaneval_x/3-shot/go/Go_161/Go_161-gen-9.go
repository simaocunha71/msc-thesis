    result := make([]byte, 0)
    is_upper := false

    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            if is_upper {
                result = append(result, byte(c - 32))
                is_upper = false
            } else {
                result = append(result, byte(c + 32))
                is_upper = true
            }
        } else if c >= 'A' && c <= 'Z' {
            if is_upper {
                result = append(result, c)
            } else {
                result = append(result, byte(c - 32))
                is_upper = true
            }
        } else {
            result = append(result, c)
        }
    }
    if len(result) == 0 {
        return reverse(s)
    }
    return string(result)
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}