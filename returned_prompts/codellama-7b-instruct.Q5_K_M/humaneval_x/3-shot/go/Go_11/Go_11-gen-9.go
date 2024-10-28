    result := make([]byte, len(a))
    for i, v := range a {
        if v == '1' && b[i] == '1' {
            result[i] = '0'
        } else if v == '1' || b[i] == '1' {
            result[i] = '1'
        } else {
            result[i] = '0'
        }
    }
    return string(result)
}



