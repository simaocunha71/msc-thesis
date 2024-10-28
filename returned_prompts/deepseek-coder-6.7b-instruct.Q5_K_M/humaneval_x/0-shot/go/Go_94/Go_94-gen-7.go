    var largestPrime, sum int
    var primes = make(map[int]bool)

B:
    for _, v := range lst {
        if isPrime(v) && v > largestPrime {
            largestPrime = v
        }
    }

C:
    if largestPrime == 0 {
        return 0
    }

D:
    for largestPrime > 0 {
        sum += largestPrime % 10
        largestPrime /= 10
    }

    return sum
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n <= 3 {
        return true
    }
    if n % 2 == 0 || n % 3 == 0 {
        return false
    }
    i := 5
    for i * i <= n {
        if n % i == 0 || n % (i + 2) == 0 {
            return false
        }
        i += 6
    }
    return true
}

// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
// 
