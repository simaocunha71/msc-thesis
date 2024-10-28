    var result []int
    for _, value := range values {
        switch value.(type) {
        case int:
            result = append(result, value.(int))
        }
    }
    return result
}