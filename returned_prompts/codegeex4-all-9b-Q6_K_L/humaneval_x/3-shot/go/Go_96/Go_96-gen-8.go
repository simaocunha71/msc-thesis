    result := make([]int, 0)

    for i := 2; i < n; i++ {
        if IsPrime(i) {
            result = append(result, i)
        }
    }
    return result
}

func IsPrime(n int) bool {
    for i := 2; i < n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

