    if n > m {
        return -1
    }
    var sum int
    for i := n; i <= m; i++ {
        sum += i
    }
    avg := int(math.Round(float64(sum) / float64(m-n+1)))
    return fmt.Sprintf("%b", avg)
}
