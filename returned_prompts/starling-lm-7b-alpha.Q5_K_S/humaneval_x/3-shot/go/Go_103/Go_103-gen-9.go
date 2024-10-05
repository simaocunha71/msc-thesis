    if n > m {
        return -1
    }

    avg := (n + m) / 2

    result := math.Round(float64(avg))
    return fmt.Sprintf("0b%d", result)
}



