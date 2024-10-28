    if len(lst) == 0 {
        return nil
    }

    sort.Ints(lst)

    for i, v := range lst {
        if i == len(lst) - 1 {
            return nil
        }

        if v == lst[i + 1] {
            continue
        }
        return v
    }

    return nil
}



