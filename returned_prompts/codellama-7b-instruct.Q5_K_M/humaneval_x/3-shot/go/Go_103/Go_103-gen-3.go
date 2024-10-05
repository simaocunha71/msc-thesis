    if n > m {
        return -1
    }

    sum := n + m
    avg := float64(sum) / 2
    rounded := math.Round(avg)
    return fmt.Sprintf("0b%b", int(rounded))
}



