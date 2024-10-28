    if len(lst) < 2 {
        return nil
    }
    // Sort the list
    sort.Ints(lst)
    // Next smallest is the second element
    return lst[1]
}



