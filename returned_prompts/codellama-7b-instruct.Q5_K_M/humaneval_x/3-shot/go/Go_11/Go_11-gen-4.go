    result := make([]rune, len(a))

    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result[i] = '0'
        } else {
            result[i] = '1'
        }
    }
    return string(result)
}



