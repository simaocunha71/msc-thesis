    sort.Ints(l)
    i := 0
    for _, v := range l {
        if l[i] != v {
            i++
            l[i] = v
        }
    }
    return l[:i+1]
}



