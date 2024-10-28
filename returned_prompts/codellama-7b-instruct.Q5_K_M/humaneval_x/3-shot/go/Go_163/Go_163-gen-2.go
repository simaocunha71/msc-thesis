    result := make([]int, 0)
    for i := a; i <= b; i++ {
        if i%2 == 0 && i >= a && i <= b {
            result = append(result, i)
        }
    }
    return result
}



