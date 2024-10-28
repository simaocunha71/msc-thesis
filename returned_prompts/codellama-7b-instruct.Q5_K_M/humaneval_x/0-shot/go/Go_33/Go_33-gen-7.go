    for i := range l {
        if i%3 == 0 {
            sort.Ints(l[i:i+3])
        }
    }
    return l
}
