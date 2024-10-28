    result := 0
    for _, v := range lst {
        if isPrime(v) {
            result += sum_digits(v)
        }
    }
    return result
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n <= 3 {
        return true
    }

    if n%2 == 0 || n%3 == 0 {
        return false
    }

    i := 5
    for ; i * i <= n; i += 6 {
        if n%i == 0 || n%(i + 2) == 0 {
            return false
        }
    }
    return true
}

func sum_digits(n int) int {
    sum := 0
    for n != 0 {
        sum += n % 10
        n /= 10
    }
    return sum
}



