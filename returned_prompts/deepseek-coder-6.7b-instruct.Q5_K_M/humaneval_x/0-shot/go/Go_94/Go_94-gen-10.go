    maxPrime := -1
    for _, v := range lst {
        if v > maxPrime && isPrime(v) {
            maxPrime = v
        }
    }
    if maxPrime == -1 {
        return 0
    }
    sum := 0
    for maxPrime != 0 {
        sum += maxPrime % 10
        maxPrime /= 10
    }
    return sum
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n == 2 {
        return true
    }
    if n%2 == 0 {
        return false
    }
    sqrtN := int(math.Sqrt(float64(n)))
    for i := 3; i <= sqrtN; i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}

This code checks each number in the list to see if it's a prime number. If it is, it checks if it's larger than the current maxPrime. If it is, it sets