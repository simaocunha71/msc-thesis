    for i := 1; i < len(l); i+=2 {
        sort.Ints(l[i:i+2])
    }
    return l
}



