    result := make([]int, len(numbers))
    result[0] = numbers[0]
    for i := 1; i < len(numbers); i++ {
        result[i] = int(math.Max(float64(result[i-1]), float64(numbers[i])))
    }
    return result
}