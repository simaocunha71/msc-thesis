    sort.Ints(l)
    n := len(l)
    mid := n / 2
    if n % 2 == 0 {
        return float64(l[mid-1] + l[mid]) / 2.0
    } else {
        return float64(l[mid])
    }
}