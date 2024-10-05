    if n > m {
        return -1
    }
    avg := math.Round(float64(n + m) / 2)
    return fmt.Sprintf("0b%b", int(avg))
}



