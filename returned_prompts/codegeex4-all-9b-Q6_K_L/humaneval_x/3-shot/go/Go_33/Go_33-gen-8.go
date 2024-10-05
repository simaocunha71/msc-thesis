    sort.Slice(l[2:len(l):3], func(i, j int) bool {
        return l[i] < l[j]
    })
    return l
}

