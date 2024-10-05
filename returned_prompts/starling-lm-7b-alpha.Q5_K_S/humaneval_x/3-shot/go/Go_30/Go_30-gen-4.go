    result := make([]int, 0)
    for _, n := range l {
        if n > 0 {
            result = append(result, n)
        }
    }
    return result
}



