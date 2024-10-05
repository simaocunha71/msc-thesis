    for i := 2; i < math.Sqrt(float64(n)); i++ {
        if n % i == 0 {
            continue A
        }
    }
    return []int{n}
}
