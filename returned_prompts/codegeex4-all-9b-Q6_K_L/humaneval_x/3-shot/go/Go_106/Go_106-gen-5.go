    result := make([]int, 0)
    var current int = 1
    for i := 1; i <= n; i++ {
        if i % 2 == 0 {
            current *= i
        }else{
            current = 0
            for j := 1; j <= i; j++ {
                current += j
            }
        }
        result = append(result, current)
    }
    return result
}

