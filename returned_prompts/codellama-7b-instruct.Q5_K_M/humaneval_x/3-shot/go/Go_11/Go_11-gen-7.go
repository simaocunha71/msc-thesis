    result := make([]byte, len(a))

    for i := 0; i < len(a); i++ {
        if a[i] != b[i] {
            result[i] = '1'
        } else {
            result[i] = '0'
        }
    }

    return string(result)
}



