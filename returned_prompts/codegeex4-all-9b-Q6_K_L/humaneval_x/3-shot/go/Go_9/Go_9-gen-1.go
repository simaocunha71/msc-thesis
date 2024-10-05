    max := numbers[0]
    result := make([]int, 0)
    result = append(result, max)
    for _, n := range numbers{
        if n > max{
            max = n
        }
        result = append(result, max)
    }
    return result
}



