    var result []int = []int{}
    for i := 2; i <= n; i++ {
        if n % i == 0 {
            result = append(result, i)
            n /= i
        }
    }
    return result
}



