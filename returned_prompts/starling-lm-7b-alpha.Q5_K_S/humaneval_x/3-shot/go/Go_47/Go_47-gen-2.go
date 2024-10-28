    sort.Ints(l)
    len_l := len(l)
    if len_l%2 == 0 {
        return float64(l[len_l/2 - 1] + l[len_l/2]) / 2.0
    } else {
        return float64(l[len_l/2])
    }
}



