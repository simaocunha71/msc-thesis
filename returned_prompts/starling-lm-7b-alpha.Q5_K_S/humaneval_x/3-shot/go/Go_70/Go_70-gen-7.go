    for i, _ := range lst {
        lst[i] = sort.IntSlice(lst).SortStable()
    }
    return lst
}



