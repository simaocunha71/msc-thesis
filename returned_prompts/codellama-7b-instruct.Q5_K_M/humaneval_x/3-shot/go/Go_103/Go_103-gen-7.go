    if n > m {
        return -1
    }
    avg := float64(n + m) / 2
    rounded_avg := math.Round(avg)
    binary_avg := fmt.Sprintf("%b", int(rounded_avg))
    return binary_avg
}



