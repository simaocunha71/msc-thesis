    var largest_prime int = 0
    for _, number := range lst {
        if IsPrime(number) && number > largest_prime {
            largest_prime = number
        }
    }
    result := 0
    for _, c := range strconv.Itoa(largest_prime) {
        d, _ := strconv.Atoi(string(c))
        result += d
    }
    return result
}

func IsPrime(n int) bool {

    if n == 1 {
        return false
    }
    if n == 2 {
        return true
    }
    for i := 2; i < int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}

