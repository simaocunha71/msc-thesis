    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i % 2 == 0 {
            result[i] = fact(i)
        } else {
            result[i] = sum(i)
        }
    }
    return result
}

func fact(i int) int {
    res := 1
    for j := 1; j <= i; j++ {
        res *= j
    }
    return res
}

func sum(i int) int {
    res := 0
    for j := 1; j <= i; j++ {
        res += j
    }
    return res
}