    result := make([]int, n)
    stones := n

    for i := 0; i < n; i++ {
        result[i] = stones
        if stones % 2 == 0 {
            stones += 2
        } else {
            stones += 2
        }
    }
    return result
}



