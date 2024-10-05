    if n > m {
        return -1
    }
    sum := 0
    count := 0
    for i := n; i <= m; i++ {
        sum += i
        count++
    }
    avg := sum / count
    rounded := math.Round(float64(avg))
    bin := fmt.Sprintf("%b", int(rounded))
    return bin
}