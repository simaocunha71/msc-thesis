    result := make([]int, 0)
    for _, i := range l {
        if i > 0 {
            result = append(result, i)
        }
    }
    return result
}

