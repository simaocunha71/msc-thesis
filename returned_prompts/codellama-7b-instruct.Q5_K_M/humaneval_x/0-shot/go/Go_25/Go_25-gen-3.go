    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        for n % i == 0 {
            n /= i
            goto A
        }
    }
    return []int{n}
}

