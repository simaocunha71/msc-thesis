    if n > m {
        return -1
    }

    avg := float64(n + m) / 2
    return int(math.Round(avg))
}
