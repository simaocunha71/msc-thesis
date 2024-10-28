    result := 1
    for i := int64(1); i <= int64(n); i++ {
        result *= i
    }
    return int(result)
}



