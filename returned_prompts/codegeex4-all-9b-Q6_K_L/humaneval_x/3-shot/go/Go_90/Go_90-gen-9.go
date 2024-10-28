    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] != lst[i+1] {
            return lst[i+1]
        }
    }
    return nil
}



