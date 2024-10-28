    if len(l) == 0{
        return 0
    }
    max := l[0]
    for _, e := range l{
        if e > max{
            max = e
        }
    }
    return max
}



