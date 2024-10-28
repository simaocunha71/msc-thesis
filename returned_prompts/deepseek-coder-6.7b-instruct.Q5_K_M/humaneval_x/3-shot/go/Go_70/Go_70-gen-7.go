    sort.Ints(lst)
    for i := 1; i < len(lst); i += 2 {
        lst[i], lst[len(lst)-i-1] = lst[len(lst)-i-1], lst[i]
    }
    return lst
}



