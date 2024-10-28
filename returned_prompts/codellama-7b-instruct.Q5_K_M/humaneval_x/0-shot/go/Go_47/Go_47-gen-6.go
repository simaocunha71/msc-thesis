
    // sort l in ascending order
    sort.Ints(l)

    // Get the middle index
    m := len(l) / 2

    // If length is odd, return middle value
    if len(l)%2 != 0 {
        return float64(l[m])
    }

    // If length is even, return average of middle two values
    return float64(l[m-1]+l[m]) / 2
}