    sort.Slice(l, func(i, j int) bool {
        return (i % 3) == (j % 3) && l[i] < l[j]
    })
    return l
}



