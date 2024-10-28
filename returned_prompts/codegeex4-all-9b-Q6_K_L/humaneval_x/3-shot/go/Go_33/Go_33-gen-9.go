    var third []int
    for i := 2; i < len(l); i += 3 {
        third = append(third, l[i])
    }
    sort.Ints(third)

    for i := 2; i < len(l); i += 3 {
        l[i] = third[i/3]
    }
    return l
}



