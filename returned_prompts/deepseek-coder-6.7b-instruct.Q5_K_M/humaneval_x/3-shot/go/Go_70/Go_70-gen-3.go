    sort.Ints(lst)
    for i := 0; i < len(lst)/2; i++ {
        lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
    }
    return lst
}



