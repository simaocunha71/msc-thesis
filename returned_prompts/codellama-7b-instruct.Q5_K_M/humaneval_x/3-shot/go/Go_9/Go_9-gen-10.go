    result := make([]int, len(numbers))

    for i, n := range numbers {
        if i == 0 {
            result[i] = n
        } else {
            result[i] = int(math.Max(float64(n), float64(result[i-1])))
        }
    }
    return result
}



