    if len(lst) < 2{
        return nil
    }
    // Sort the list
    sort.Ints(lst)
    // Get the second element of the sorted list
    return lst[1]
}



