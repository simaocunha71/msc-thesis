    sort.Ints(l)
    middle := len(l) / 2
    if len(l)%2 == 0 {
        return float64(l[middle] + l[middle-1]) / 2
    }
    return float64(l[middle])
}



