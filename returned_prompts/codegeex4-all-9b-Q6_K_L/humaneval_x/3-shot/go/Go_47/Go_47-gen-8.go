    sort.Ints(l)
    var median float64
    if len(l)%2 == 0 {
        median = float64(l[len(l)/2-1]+l[len(l)/2]) / 2
    } else {
        median = float64(l[len(l)/2])
    }
    return median
}



