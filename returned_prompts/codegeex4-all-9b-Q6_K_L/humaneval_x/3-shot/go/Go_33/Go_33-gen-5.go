    third := l[2:len(l):2]
    sort.Ints(third)
    for i, _ := range third {
        l[2*i+2] = third[i]
    }
    return l
}



