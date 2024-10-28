    sort.Ints(l)
    var res []int
    for i := 0; i < len(l); i++ {
        if i > 0 && l[i] == l[i-1] {
            continue
        }
        res = append(res, l[i])
    }
    return res
}

