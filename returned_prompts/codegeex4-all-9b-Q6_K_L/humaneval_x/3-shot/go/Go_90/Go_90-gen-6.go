    if len(lst) < 2 {
        return nil
    }

    lst = append(lst, math.MaxInt64)
    sort.Ints(lst)
    return lst[1]
}



