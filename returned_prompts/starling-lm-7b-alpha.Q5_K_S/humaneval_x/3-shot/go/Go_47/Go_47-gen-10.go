    n := len(l)
    sort.Slice(l, func(i int, j int) bool { return l[i] < l[j] })
    return float64(l[n/2])
}



