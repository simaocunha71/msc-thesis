    if len(l) == 0 {
        panic("empty list")
    }

    result := l[0]
    for i := 1; i < len(l); i++ {
        if l[i] > result {
            result = l[i]
        }
    }
    return result
}



