    sort.Float64s(l)
    n := len(l)
    if n % 2 == 1 {
        return float64(l[n/2])
    } else {
        return (l[n/2-1] + l[n/2]) / 2
    }
}