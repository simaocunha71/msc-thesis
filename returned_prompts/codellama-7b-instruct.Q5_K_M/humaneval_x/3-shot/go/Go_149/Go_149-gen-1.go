    // sort by length
    sort.Slice(lst, func(i, j int) bool {
        return len(lst[i]) < len(lst[j])
    })
    // sort by alphabet
    sort.Strings(lst)

    return lst
}



