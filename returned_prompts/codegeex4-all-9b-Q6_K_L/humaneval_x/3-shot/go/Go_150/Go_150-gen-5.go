    if isPrime(n){
        return x
    }else{
        return y
    }
}

func isPrime(n int) bool {
    for i := 2; i < n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

