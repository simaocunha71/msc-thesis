    var evens []int
    var odds []int
    for i, v := range l {
        if i%2 == 0 {
            evens = append(evens, v)
        } else {
            odds = append(odds, v)
        }
    }
    sort.Ints(evens)
    result := make([]int, len(l))
    for i, v := range evens {
        result[i*2] = v
    }
    for i, v := range odds {
        result[i*2+1] = v
    }
    return result
}



