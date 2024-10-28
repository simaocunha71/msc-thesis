    sort.Ints(l)
    if len(l)%2 == 0 {
        return float64(l[len(l)/2])
    }
    return float64(l[(len(l)-1)/2])
}



