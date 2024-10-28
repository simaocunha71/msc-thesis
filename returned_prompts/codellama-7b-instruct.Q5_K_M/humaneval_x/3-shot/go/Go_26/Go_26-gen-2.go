    result := make([]int, 0)
    for _, number := range numbers {
        if !ContainsInt(result, number) {
            result = append(result, number)
        }
    }
    return result
}



