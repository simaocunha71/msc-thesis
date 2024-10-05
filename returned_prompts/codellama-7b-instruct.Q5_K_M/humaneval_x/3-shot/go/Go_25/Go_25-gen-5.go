    result := make([]int, 0)
    divisor := 2

    for n > 1 {
        for n % divisor == 0 {
            result = append(result, divisor)
            n = n / divisor
        }
        divisor += 1
    }
    return result
}



