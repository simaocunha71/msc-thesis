    if n>m {
        return -1
    }
    total := 0
    for i := n; i <= m; i++ {
        total += i
    }
    average := float64(total) / float64(m-n+1)
    rounded := math.Round(average)
    return fmt.Sprintf("0b%b", int(rounded))
}



