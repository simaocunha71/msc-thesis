    for i, num := range arr[:k] {
        if num >= 100 {
            continue A
        }
        if num >= 10 {
            return num
        }
        return num
    }
    return 0
}
