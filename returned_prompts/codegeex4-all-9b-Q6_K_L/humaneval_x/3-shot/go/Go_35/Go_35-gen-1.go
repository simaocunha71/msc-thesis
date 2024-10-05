    if len(l) == 0 {
        return 0
    }
    max := l[0]
    for _, e := range l {
        if max < e {
            max = e
        }
    }
    return max
}



