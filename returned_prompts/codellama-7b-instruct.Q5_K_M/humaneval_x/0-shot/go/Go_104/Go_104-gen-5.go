    for i := range x {
        for j := range x {
            if x[i] == x[j] && i != j {
                continue A
            }
        }
        if strconv.Itoa(x[i])[0]%2 == 0 {
            continue A
        }
        y = append(y, x[i])
    }
    sort.Ints(y)
    return y
}
