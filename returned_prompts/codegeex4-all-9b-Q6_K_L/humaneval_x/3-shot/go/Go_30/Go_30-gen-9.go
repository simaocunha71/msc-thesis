    result := make([]int, 0)
    for _, value := range l {
        if value > 0 {
            result = append(result, value)
        }
    }
    return result
}



