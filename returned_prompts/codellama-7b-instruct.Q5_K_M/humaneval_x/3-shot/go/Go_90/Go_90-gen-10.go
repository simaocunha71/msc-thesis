    if len(lst) < 2{
        return nil
    }
    var smallest = lst[0]
    for i:=1; i<len(lst); i++{
        if lst[i] < smallest{
            smallest = lst[i]
        }
    }
    var second_smallest = -1
    for i:=0; i<len(lst); i++{
        if lst[i] > smallest{
            if second_smallest == -1{
                second_smallest = lst[i]
            }
        }
    }
    if second_smallest != -1{
        return second_smallest
    }
    return nil
}



