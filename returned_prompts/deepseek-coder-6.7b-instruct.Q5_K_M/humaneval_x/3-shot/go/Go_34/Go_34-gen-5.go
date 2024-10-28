    sort.Ints(l)
    res := l[:1]

    for _, v := range l[1:] {
        if v != res[len(res)-1] {
            res = append(res, v)
        }
    }
    return res
}



