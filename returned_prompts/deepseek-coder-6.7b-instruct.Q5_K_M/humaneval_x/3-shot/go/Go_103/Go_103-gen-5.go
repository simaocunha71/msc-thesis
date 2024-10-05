    if n > m {
        return -1
    }

    avg := int(math.Round(float64(n + m) / 2.0))
    return fmt.Sprintf("0b%b", avg)
}



