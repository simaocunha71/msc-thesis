    result := make([]int, 0)
    i := 2

    for i <= math.Sqrt(float64(n)) {
        count := 0
        for n % i == 0 {
            count++
            n /= i
        }
        if count > 0 {
            result = append(result, int(i))
            for count > 0 {
                count--
                result = append(result, int(i))
            }
        }
        i++
    }
    if n > 1 {
        result = append(result, n)
    }
    return result
}