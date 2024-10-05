    sort.Slice(l[1::2], func(i, j int) bool {
        return l[2*i] < l[2*j]
    })
    return l
}