    if n<=0{
        return make([]int, 0)
    }

    result := make([]int, 0)
    for i := 2; i < n; i++ {
        if isPrime(i){
            result = append(result, i)
        }
    }
    return result
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

