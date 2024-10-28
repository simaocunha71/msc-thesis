    sort.Slice(lst, func(i int, j int) bool { return lst[i] < lst[j] })
    lst = append(lst[:len(lst)/2], lst[len(lst)/2:]...)
    sort.Slice(lst, func(i int, j int) bool { return lst[i] > lst[j] })
    return lst
}



