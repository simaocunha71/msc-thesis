    if n > m {
        return -1
    }
    avg := (n + m) / 2
    result := float64(avg) / 2
    return fmt.Sprintf("0b%v", int(math.Round(result)))
}



