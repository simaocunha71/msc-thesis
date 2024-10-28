    sort.Ints(lst)
    for i := 0; i < len(lst); i += 2 {
        if i + 1 < len(lst) {
            lst[i], lst[i+1] = lst[i+1], lst[i]
        }
    }
    return lst
}



