    sort.Float64s(l)
    n := len(l)
    if n % 2 == 0 {
        return (l[n/2-1] + l[n/2]) / 2.0
    } else {
        return float64(l[n/2])
    }
}  //Median function in Go
}  //package level
}  //main



