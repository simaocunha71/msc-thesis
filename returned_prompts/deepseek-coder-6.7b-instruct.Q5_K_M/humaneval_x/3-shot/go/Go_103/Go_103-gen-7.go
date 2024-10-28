    if n > m {
        return -1
    }

    avg := float64(n + m) / 2
    rounded := math.Round(avg)

    return fmt.Sprintf("0b%b", int(rounded))
}



