    for i := 1; i < len(l); i += 3 {
        if l[i] <= l[i-1] {
            l[i], l[i-1] = l[i-1], l[i]
        }
    }

    sort.Ints(l)
    return l
}
