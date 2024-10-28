    l3 := make([]int, 0)
    for i, v := range l {
        if i % 3 == 2 {
            l3 = append(l3, v)
        }
    }
    sort.Ints(l3)

    for i, v := range l {
        if i % 3 == 2 {
            l[i] = l3[0]
            l3 = l3[1:]
        }
    }
    return l
}