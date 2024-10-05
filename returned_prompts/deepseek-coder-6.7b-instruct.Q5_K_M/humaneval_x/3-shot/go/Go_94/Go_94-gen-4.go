    var maxPrime int = 0
    for _, num := range lst  {
        if IsPrime(num) && num > maxPrime  {
            maxPrime = num
        }
    }
    digitSum := 0
    for maxPrime > 0 {
        digit := maxPrime % 10
        digitSum += digit
        maxPrime /= 10
    }
    return digitSum
}

func IsPrime(n int) bool {
    if n == 2 || n == 3 {
        return true
    }
    if n < 2 || n%2 == 0 {
        return false
    }
    for i := 3; i*i <= n; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}



