    result := make([]int, len(numbers)*2-1)
    for i, number := range numbers {
        result[i*2] = number
        result[i*2+1] = delimeter
    }
    return result
}



