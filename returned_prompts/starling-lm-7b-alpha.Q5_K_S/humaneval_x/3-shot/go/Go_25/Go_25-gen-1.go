    var result []int = make([]int, 0)
    for i := 2; i <= n; i++ {
        for ; n % i == 0; n /= i {
            result = append(result, i)
        }
    }
    return result
}



