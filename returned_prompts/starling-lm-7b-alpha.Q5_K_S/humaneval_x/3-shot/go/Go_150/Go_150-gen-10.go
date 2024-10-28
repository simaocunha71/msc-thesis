    if n == 2 || n == 3 || n == 5 {
        return y
    }

    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n % i == 0 {
            return y
        }
    }
    return x
}



