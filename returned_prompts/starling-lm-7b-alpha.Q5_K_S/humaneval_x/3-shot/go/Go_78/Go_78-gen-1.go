    result := 0
    for _, c := range num {
        switch {
        case c >= '0' && c <= '9':
            v := int(c - '0')
            if v > 1 {
                result += v%2 == 0
            }else {
                result += 0
            }
        case c >= 'A' && c <= 'F':
            v := int(c - 'A') + 10
            if v > 1 {
                result += v%2 == 0
            }else {
                result += 0
            }
        }
    }
    return result
}



