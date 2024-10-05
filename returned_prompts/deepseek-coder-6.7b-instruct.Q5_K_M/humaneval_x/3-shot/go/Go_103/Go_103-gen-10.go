    if n > m {
        return -1
    }

    avg := float64(n+m) / 2.0
    rounded := math.Round(avg)
    binary := fmt.Sprintf("%b", int(rounded))

    return "0b" + binary
}



