    if n > m {
        return -1
    }

    sum := n + m
    avg := sum / 2
    roundedAvg := math.Round(avg)

    return fmt.Sprintf("0b%b", roundedAvg)
}


