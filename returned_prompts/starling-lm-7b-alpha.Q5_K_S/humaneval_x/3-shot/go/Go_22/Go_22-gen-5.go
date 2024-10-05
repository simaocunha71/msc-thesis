    result := make([]int, 0)
    for _, v := range values {
        var i int = int(v.(float64))
        if i == int(v.(float64)){
            result = append(result, i)
        }
    }
    return result
}



