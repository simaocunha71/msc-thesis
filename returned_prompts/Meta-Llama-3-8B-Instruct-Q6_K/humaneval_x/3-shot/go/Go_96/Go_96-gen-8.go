    result := make([]int, 0)
    for i := 2; i < n; i++ {
        if IsPrime(i) {
            result = append(result, i)
        }
    }
    return result
}

func IsPrime(num int) bool {
    if num < 2 {
        return false
    }
    for i := 2; i * i <= num; i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}