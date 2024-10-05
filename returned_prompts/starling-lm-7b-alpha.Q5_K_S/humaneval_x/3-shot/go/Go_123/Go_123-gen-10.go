    result := make([]int, 0)

    for i := 1; i <= n; i++ {
        current := i
        for current % 2 == 0 {
            current /= 2
        }
        if current % 2 == 1 {
            result = append(result, current)
        }
    }
    sort.Ints(result)
    return result
}



