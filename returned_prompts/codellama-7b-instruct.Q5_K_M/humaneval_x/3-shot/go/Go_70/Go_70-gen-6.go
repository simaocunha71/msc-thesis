    if len(lst) == 0{
        return lst
    }

    min_index := 0
    max_index := 0
    for i, v := range lst{
        if v > lst[max_index]{
            max_index = i
        }
        if v < lst[min_index]{
            min_index = i
        }
    }
    temp := lst[max_index]
    lst[max_index] = lst[min_index]
    lst[min_index] = temp

    return append(StrangeSortList(lst[:min_index]),StrangeSortList(lst[min_index+1:])...)
}



