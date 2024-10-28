    if len(l) == 0 {
        panic("The list is empty")
    }

    max := l[0]
    for i := 1; i < len(l); i++ {
        if l[i] > max {
            max = l[i]
        }
    }
    return max
}

