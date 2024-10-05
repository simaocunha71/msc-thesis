    sort.Ints(l)
    l = l[:len(l):len(l)]
    for i := 1; i < len(l); i++ {
        if l[i] == l[i-1] {
            l = append(l[:i], l[i+1:]...)
            i--
        }
    }
    return l
}



