    sort.Ints(l)
    n := len(l)
    if n % 2 == 1 {
        return float64(l[n/2])
    } else {
        mid1 := l[n/2 - 1]
        mid2 := l[n/2]
        return float64((mid1 + mid2) / 2)
    }
}