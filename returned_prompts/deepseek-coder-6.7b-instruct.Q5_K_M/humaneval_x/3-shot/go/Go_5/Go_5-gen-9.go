    result := make([]int, 0, len(numbers)*2-1)
    for i, num := range numbers {
        result = append(result, num)
        if i != len(numbers)-1 {
            result = append(result, delimeter)
        }
    }
    return result
}



