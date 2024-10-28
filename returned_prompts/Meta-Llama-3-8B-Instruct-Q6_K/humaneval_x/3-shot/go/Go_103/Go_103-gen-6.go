    if n > m {
        return -1
    }
    total := 0
    count := 0
    for i := n; i <= m; i++ {
        total += i
        count++
    }
    avg := total / count
    rounded_avg := math.Round(float64(avg))
    binary := fmt.Sprintf("%b", int(rounded_avg))
    return binary
}