    var primeCheck = func(n int) bool {
        if n == 2 {
            return true
        }
        if n < 2 || n % 2 == 0 {
            return false
        }
        for i := 3; i * i <= n; i += 2 {
            if n % i == 0 {
                return false
            }
        }
        return true
    }

    count := 0
    for i := 2; i <= a; i++ {
        if a % i == 0 && primeCheck(i) {
            count++
        }
        if count > 3 {
            return false
        }
    }
    return count == 3
}



