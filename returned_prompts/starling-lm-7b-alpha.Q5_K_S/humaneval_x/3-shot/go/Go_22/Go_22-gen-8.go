    result := make([]int, 0)
    for _, v := range values {
        if v != nil {
            if v.(int) != 0 {
                result = append(result, v.(int))
            }
        }
    }
    return result
}



