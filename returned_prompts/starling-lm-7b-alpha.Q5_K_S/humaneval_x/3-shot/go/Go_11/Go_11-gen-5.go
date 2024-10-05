    result := make([]rune, 0)

    for _, c := range a {
        if c == '1' {
            if b == '1' {
                result = append(result, '0')
            } else {
                result = append(result, '1')
            }
        } else {
            if b == '1' {
                result = append(result, '1')
            } else {
                result = append(result, '0')
            }
        }
    }
    return string(result)
}



