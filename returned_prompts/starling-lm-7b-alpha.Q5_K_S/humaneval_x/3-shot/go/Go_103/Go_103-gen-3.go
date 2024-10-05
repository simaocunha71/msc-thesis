    if n > m {
        return -1
    }
    avg := int((n + float64(m)) / 2)
    result := fmt.Sprintf("%b", avg)
    return result
}



