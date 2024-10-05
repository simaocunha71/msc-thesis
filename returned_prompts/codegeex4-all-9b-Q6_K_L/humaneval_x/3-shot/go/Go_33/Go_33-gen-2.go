    sort.Slice(l, func(i, j int) bool {
        return l[i]%3 < l[j]%3
    })
    return l
}



