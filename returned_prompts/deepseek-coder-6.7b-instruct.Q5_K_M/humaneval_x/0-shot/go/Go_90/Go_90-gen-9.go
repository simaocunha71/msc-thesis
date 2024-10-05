    if len(lst) < 2 {
        return nil
    }

    // sort the list
    sort.Ints(lst)

    // search for the 2nd smallest element
    for i := 1; i < len(lst); i++ {
        if lst[i] != lst[0] {
            return lst[i]
        }
    }

    return nil
}


