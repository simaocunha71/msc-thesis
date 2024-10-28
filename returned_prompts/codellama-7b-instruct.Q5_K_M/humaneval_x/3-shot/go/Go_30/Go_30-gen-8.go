    result := make([]int, 0)
    for _, x := range l {
        if x > 0 {
            result = append(result, x)
        }
    }
    return result
}



