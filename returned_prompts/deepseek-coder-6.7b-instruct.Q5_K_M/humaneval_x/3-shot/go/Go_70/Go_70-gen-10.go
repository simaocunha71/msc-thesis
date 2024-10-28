    sort.Ints(lst)
    res := make([]int, len(lst))
    for i, j := 0, len(lst)-1; i <= j; i, j = i+1, j-1 {
        if i == j {
            res[i] = lst[i]
        } else {
            res[i] = lst[i]
            res[j] = lst[j]
        }
    }
    return res
}



