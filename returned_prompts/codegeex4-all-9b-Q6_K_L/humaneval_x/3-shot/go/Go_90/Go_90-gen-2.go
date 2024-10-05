    if len(lst) < 2 {
        return nil
    }

    sort.Ints(lst)
    second_smallest := lst[1]

    for _, v := range lst {
        if v == second_smallest {
            return nil
        }
    }

    return second_smallest
}



