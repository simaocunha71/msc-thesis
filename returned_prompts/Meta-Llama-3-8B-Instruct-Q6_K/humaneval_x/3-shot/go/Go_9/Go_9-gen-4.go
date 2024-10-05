    result := make([]int, len(numbers))
    max_so_far := numbers[0]
    result[0] = max_so_far
    for i := 1; i < len(numbers); i++ {
        max_so_far = int(math.Max(float64(max_so_far), float64(numbers[i])))
        result[i] = max_so_far
    }
    return result
}