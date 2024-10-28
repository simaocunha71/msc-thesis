    if n > m {
        return -1
    }
    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := math.Round(float64(sum) / float64(m-n+1))
    return fmt.Sprintf("0b%b", avg)
}
}}



