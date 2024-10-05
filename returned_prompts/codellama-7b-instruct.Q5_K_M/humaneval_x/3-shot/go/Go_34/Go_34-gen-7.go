    sort.Ints(l)
    for i := 0; i < len(l)-1; i++ {
        if l[i] == l[i+1] {
            l = append(l[:i], l[i+1:]...)
            i -= 1
        }
    }
    return l
}



