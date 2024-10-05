    max_prime := -1
    for _, num := range lst {
        if IsPrime(num) && num > max_prime {
            max_prime = num
        }
    }

    if max_prime == -1 {
        return 0
    }

    return SumOfDigits(max_prime)
}

func IsPrime(n int) bool {
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
    for i*i <= n {
        if n%i == 0 || n%(i+2) == 0 {
            return false
        }
        i += 6
    }
    return true
}

func SumOfDigits(n int) int {
    sum := 0
    for n > 0 {
        digit := n % 10
        sum += digit
        n /= 10
    }
    return sum
}



