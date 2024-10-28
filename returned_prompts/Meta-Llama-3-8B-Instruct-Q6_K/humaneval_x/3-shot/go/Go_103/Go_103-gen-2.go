    if n > m {
        return -1
    }
    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := float64(sum) / float64(m-n+1)
    rounded_avg := math.Round(avg)
    binary_avg := fmt.Sprintf("%b", int(rounded_avg))
    return binary_avg
}