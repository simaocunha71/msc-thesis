    if n > m {
        return -1
    }
    sum := 0.0
    for i := float64(n); i <= float64(m); i++ {
        sum += i
    }
    avg := math.Round(sum / float64(m-n+1))
    bin := fmt.Sprintf("%b", int(avg))
    return bin
}