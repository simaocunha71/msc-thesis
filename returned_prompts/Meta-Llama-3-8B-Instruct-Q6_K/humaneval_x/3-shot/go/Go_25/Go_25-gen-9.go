    result := make([]int, 0)
    i := 2
    for i * i <= n {
        count := 0
        for n % i == 0 {
            count++
            n = n / i
        }
        if count > 0 {
            result = append(result, i)
            for count > 0 {
                result = append(result, i)
                count--
            }
        }
        i++
    }
    if n > 1 {
        result = append(result, n)
    }
    return result
}