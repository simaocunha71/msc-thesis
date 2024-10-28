    result := make([]int, n)
    if n == 0 {
        return result
    }

    result[0] = 1
    for i := 1; i < n; i++ {
        if i%2 == 0 {
            result[i] = i
            for j := 1; j <= i; j++ {
                result[i] *= j
            }
        } else {
            result[i] = 0
            for j := 1; j <= i; j++ {
                result[i] += j
            }
        }
    }
    return result
}

