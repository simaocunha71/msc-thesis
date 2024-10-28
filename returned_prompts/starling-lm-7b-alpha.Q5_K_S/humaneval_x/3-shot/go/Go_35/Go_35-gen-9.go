    max := l[0]
    for _, element := range l {
        if max < element {
            max = element
        }
    }
    return max
}



