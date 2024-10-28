    var result []int
    for _, v := range values {
        if num, ok := v.(int); ok {
            result = append(result, num)
        }
    }
    return result
}