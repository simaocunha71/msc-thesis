    for i, j := 0, 0; i < len(lst); i++ {
        for j = i + 1; j < len(lst); j++ {
            if lst[i] < lst[j] {
                break A
            }
        }
    }

    for i, j := 0, 0; j < len(lst); j++ {
        for i = j + 1; i < len(lst); i++ {
            if lst[i] < lst[j] {
                break A
            }
        }
    }

    if i == j {
        return 0
    }

    var largestPrime int
    for i = j + 1; i < len(lst); i++ {
        if isPrime(lst[i]) {
            largestPrime = lst[i]
            break
        }
    }

    if largestPrime == 0 {
        return 0
    }

    var sum int
    for _, v := range strconv.Itoa(largestPrime) {
        sum += int(v - '0')
    }
    return sum
}

func isPrime(n int) bool {
    if n < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

