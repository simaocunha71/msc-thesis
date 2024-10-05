    sort.Ints(l)
    var size int = len(l)
    if size % 2 == 0 {
        return (float64(l[size / 2 - 1]) + float64(l[size / 2])) / 2.0
    } else {
        return float64(l[size / 2])
    }
}



