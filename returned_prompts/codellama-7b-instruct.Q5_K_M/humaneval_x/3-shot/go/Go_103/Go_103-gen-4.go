    if n > m{
        return -1
    }
    sum := 0
    for i := n; i <= m; i++{
        sum += i
    }
    avg := sum / (m - n + 1)
    return fmt.Sprintf("0b%b", math.Round(avg))
}



