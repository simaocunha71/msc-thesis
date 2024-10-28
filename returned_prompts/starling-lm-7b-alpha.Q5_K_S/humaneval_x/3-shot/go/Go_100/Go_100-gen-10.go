    result := make([]int, n)
    current := n
    for i := 0; i < n; i++ {
        if current % 2 == 0 {
            result[i] = current + 1
        }else {
            result[i] = current + 2
        }
        current = result[i]
    }
    return result
}



