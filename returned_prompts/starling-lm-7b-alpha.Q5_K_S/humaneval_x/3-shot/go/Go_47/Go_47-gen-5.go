    length := len(l)
    if length < 2 {
        return float64(l[0])
    }
    sort.Ints(l)
    index := (length - 1) / 2
    if length % 2 == 0 {
        return float64(l[index] + l[index-1]) / 2.0
    } else {
        return float64(l[index])
    }
}



