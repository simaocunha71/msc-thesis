    sort.Ints(l)
    n := len(l)

    for i := 0; i < n-1; i++ {
        if l[i] == l[i+1] {
            l = append(l[:i], l[i+1:]...)
            n -= 1
            i -= 1
        }
    }
    return l
}



