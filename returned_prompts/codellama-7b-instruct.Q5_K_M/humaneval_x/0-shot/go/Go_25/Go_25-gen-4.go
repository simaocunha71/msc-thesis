    for i := 1; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return []int{i}
        }
    }
    return []int{n}
}


func Factorize(n int) []int {
    var factors []int
    for i := 2; i*i <= n; i++ {
        if n % i == 0 {
            factors = append(factors, i)
            for n % i == 0 {
                n /= i
            }
        }
    }
    if n > 1 {
        factors = append(factors, n)
    }
    return factors
}


func Factorize(n int) []int {
    var factors []int
    for i := 2; i*i <= n; i++ {
        if n % i == 0 {
            factors = append(factors, i)
            for n % i == 0 {
                n /= i
            }
        }
    }
    if n > 1 {
        factors = append(factors, n)
    }
    return factors
}


func Factorize(n int) []int {
    var factors []int
    for i := 2; i*i <= n; i++ {
        if n % i == 0 {
            factors = append(factors, i)
            for n % i == 0 {
                n /= i
            }
        }
    }
    if n > 1 {
        factors = append(factors, n)
    }
    return factors
}


func Factorize(n int) []int {
    var factors []int
    for i := 2; i*i <= n; i++ {
        if n % i == 0 {
            factors = append