    sort.Ints(l1)
    sort.Ints(l2)

    var result  []int
    for _, v := range l1 {
        if sort.SearchInts(l2, v) < len(l2) {
            result = append(result, v)
        }
    }
    return result
}



