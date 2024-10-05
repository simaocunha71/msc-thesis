    result := make([]int, 0)
    current := 2
    for current <= math.Sqrt(float64(n)) {
        if n % current == 0 {
            result = append(result, current)
            n /= current
        }else {
            current += 1
        }
    }
    if n > 1 {
        result = append(result, n)
    }
    return result
}



