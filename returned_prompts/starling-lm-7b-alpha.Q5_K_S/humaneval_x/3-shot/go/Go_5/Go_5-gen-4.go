    result := make([]int, len(numbers)*2)

    for i, n := range numbers {
        result[i*2] = n
        result[i*2+1] = delimeter
    }

    return result
}



