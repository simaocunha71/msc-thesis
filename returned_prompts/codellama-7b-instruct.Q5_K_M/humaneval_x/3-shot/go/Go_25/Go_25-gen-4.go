    result := make([]int, 0)

    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            result = append(result, i)
            n = n / i
            i = 2
        }
    }

    if n > 1 {
        result = append(result, n)
    }

    return result
}



