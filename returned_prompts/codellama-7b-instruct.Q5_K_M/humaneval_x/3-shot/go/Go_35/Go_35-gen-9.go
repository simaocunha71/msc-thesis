    if len(l) == 0 {
        return -1
    }
    max := l[0]
    for _, n := range l {
        if n > max {
            max = n
        }
    }
    return max
}



