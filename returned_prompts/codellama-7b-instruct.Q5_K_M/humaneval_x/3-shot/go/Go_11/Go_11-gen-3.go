    result := make([]byte, len(a))
    for i := 0; i < len(a); i++ {
        result[i] = a[i] ^ b[i]
    }
    return string(result)
}



