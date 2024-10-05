    if n > m {
        return -1
    }

    sum := 0
    for i := n; i <= m; i++ {
        sum += i
    }

    avg := float64(sum) / float64(m - n + 1)
    avg = math.Round(avg)
    avg = int(avg)
    avg = int(math.Log2(float64(avg)))
    return fmt.Sprintf("0b%b",avg)
}



