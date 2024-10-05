    if len(lst) < 2 {
        return nil
    }
    sort.Ints(lst)

    smallest := lst[0]
    for _, v := range lst {
        if v > smallest {
            return v
        }
    }
    return nil
}



