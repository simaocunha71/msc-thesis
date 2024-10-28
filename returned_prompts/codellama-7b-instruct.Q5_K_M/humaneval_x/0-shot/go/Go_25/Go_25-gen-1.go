for {
    if n == 1 {
        break A
    }
    for i := 2; i < int(math.Sqrt(float64(n)))+1; i++ {
        if n%i == 0 {
            n = n / i
            continue A
        }
    }
}

return []int{n}

}
