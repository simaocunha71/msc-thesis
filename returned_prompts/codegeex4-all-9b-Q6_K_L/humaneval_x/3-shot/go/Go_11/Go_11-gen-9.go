    result := make([]byte, 0)
    for i := 0; i < len(a); i++ {
        if a[i] == '1' && b[i] == '1' {
            result = append(result, '0')
        } else if a[i] == '1' || b[i] == '1' {
            result = append(result, '1')
        } else {
            result = append(result, '0')
        }
    }
    return string(result)
}

