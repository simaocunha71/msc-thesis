    max := 0
    for _, x := range lst {
        if x > max {
            max = x
        }
    }

    isPrime := func(n int) bool {
        if n <= 1 {
            return false
        }
        for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }

    if isPrime(max) {
        sum := 0
        for _, c := range strconv.Itoa(max) {
            i, _ := strconv.Atoi(string(c))
            sum += i
        }
        return sum
    }
    return 0
}



