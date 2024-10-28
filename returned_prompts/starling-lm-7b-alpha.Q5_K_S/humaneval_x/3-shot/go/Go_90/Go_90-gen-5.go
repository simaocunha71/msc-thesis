    if len(lst) < 2 {
        return nil
    }else {
        sort.Ints(lst)
        return lst[1]
    }
}



