    sort.Ints(l1)
    sort.Ints(l2)
    common := []int{}
    for _, v := range l1 {
        if sort.SearchInts(l2, v) < len(l2) {
            common = append(common, v)
        }
    }
    return common
}



