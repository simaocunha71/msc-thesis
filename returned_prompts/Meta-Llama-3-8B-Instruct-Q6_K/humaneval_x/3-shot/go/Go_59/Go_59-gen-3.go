    var maxFactor int
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        for n % i == 0 {
            maxFactor = i
            n = n / i
        }
    }
    return maxFactor
}