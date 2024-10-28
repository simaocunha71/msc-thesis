    var max int = -1
    for _, v := range lst {
        if v > max && isPrime(v) {
            max = v
        }
    }
    if max == -1 {
        return 0
    }

    sum := 0
    for _, c := range strconv.Itoa(max) {
        sum += int(c - '0')
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
    for i := 3; i <= math.Sqrt(float64(n)); i += 2 {
        if n%i == 0 {
            return false
        }
    }
    return true
}



