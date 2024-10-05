    result := make([]int, 0)
    stones := n

    for i := 0; i < n; i++ {
        result = append(result, stones)
        if i % 2 == 0 {
            stones += 1
        } else {
            stones += 2
        }
    }
    return result
}