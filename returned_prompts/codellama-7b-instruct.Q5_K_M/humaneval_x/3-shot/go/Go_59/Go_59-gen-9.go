    for i := n; i >= 2; i-- {
        if n % i == 0 && isPrime(i){
            return i
        }
    }
    return 1
}

func isPrime(n int) bool {
    if n == 2 {
        return true
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}



