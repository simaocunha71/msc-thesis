    result := make([]int, 0)

    for d := 2; d*d <= n; d++ {
        while n % d == 0 {
            result = append(result, d)
            n /= d
        }
    }

    if n > 1 {
        result = append(result, n)
    }

    return result
}



