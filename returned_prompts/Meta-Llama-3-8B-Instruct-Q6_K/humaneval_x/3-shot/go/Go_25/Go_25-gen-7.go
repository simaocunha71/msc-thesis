    result := make([]int, 0)
    i := 2

    for i * i <= n {
        count := 0
        for n % i == 0 {
            n /= i
            count++
        }
        if count > 0 {
            result = append(result, int32(i))
            for count > 0 {
                result = append(result, int32(i))
                count--
            }
        }
        i++
    }

    if n > 1 {
        result = append(result, int32(n))
    }
    return result
}  // end of function Factorize



