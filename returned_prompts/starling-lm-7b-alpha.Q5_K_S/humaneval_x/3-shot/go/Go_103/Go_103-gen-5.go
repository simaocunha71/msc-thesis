    if n > m {
        return -1
    }
    avg := (n + m) / 2
    result := (1 << uint(math.Ceil(math.Log2(float64(avg)))) + avg - 1) / (1 << uint(math.Ceil(math.Log2(float64(avg)))))
    return fmt.Sprintf("0b%d", result)
}



