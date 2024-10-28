    result := make([]byte, len(a))
    for i, c := range a {
        if c == '1' && b[i] == '1' {
            result[i] = '0'
        }else {
            result[i] = '1'
        }
    }
    return string(result)
}



