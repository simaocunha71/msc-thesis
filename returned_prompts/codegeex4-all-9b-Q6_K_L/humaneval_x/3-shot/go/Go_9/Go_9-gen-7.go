    result := make([]int, 0)
    var max int
    for _, v := range numbers {
        if v > max {
            max = v
        }
        result = append(result, max)
    }
    return result
}



