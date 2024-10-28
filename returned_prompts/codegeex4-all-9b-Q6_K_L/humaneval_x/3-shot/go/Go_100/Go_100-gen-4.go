    result := make([]int, 0)

    current := n
    for i := 0; i < n; i++ {
        result = append(result, current)
        current += 2
    }
    return result
}



