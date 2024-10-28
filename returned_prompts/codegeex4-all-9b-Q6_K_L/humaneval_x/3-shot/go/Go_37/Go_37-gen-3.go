    even := make([]int, 0)
    for i := 0; i < len(l); i+=2 {
        even = append(even, l[i])
    }
    sort.Ints(even)
    for i := 0; i < len(l); i+=2 {
        l[i] = even[i/2]
    }
    return l
}



