    result := make([]int, n)
    var level int = 1
    for i := 0; i < n; i++ {
        result[i] = level
        level += 2
    }
    return result
}



