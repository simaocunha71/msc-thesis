    sort.Ints(lst)
    for i := 1; i < len(lst); i += 2 {
        lst[i], lst[len(lst)-i] = lst[len(lst)-i], lst[i]
    }
    return lst
}



