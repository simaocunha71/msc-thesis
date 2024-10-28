    if n > m {
        return -1
    }
    sum := float64(0)
    for i := n; i <= m; i++ {
        sum += float64(i)
    }
    avg := sum / float64(m - n + 1)
    avg = math.Round(avg)
    return fmt.Sprintf("0b%b", int(avg))
}



