    result := make([]rune, len(a))
    for i, _ := range result {
        result[i] = a[i] ^ b[i]
    }
    return string(result)
}



