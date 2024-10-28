    if len(l) == 0 {
        panic("List is empty")
    }
    max := l[0]
    for _, v := range l[1:] {
        if v > max {
            max = v
        }
    }
    return max
}



