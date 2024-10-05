    sort.Ints(l)
    lenl := len(l)

    if lenl % 2 == 0 {
        return (float64(l[lenl/2-1]) + float64(l[lenl/2])) / 2.0
    } else {
        return float64(l[lenl/2])
    }
}



