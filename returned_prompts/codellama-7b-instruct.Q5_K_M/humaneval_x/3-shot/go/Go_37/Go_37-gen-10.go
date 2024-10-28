    sort.Slice(l, func(i, j int) bool {
        if i%2 == 0 && j%2 == 0 {
            return l[i] < l[j]
        }
        return false
    })
    return l
}



