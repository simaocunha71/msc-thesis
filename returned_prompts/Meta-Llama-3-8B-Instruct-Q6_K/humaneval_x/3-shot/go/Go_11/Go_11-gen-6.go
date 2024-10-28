    result := make([]byte, len(a))
    for i := range a {
        if a[i] == b[i] {
            result[i] = '0'
        } else {
            result[i] = '1'
        }
    }
    return string(result)
}