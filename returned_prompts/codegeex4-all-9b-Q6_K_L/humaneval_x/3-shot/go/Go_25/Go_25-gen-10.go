    result := make([]int, 0)
    i := 2
    for i <= n {
        if n%i == 0 {
            result = append(result, i)
            n = n / i
        } else {
            i++
        }
    }
    return result
}



