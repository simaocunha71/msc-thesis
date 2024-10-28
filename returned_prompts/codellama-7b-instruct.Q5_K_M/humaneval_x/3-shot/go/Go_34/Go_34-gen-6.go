    sort.Ints(l)
    i := 1
    for j := 1; j < len(l); j++ {
        if l[j] != l[i] {
            i++
            l[i] = l[j]
        }
    }
    return l[:i+1]
}



