    result := make([]byte, 0)
    for i := 0; i < len(a); i++ {
        result = append(result, a[i] ^ b[i])
    }
    return string(result)
}



