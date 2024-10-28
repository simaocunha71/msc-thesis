    l1,l2 := 0,0
    for _,str := range lst1 {
        l1 += len(str)
    }
    for _,str := range lst2 {
        l2 += len(str)
    }
    if l1 < l2 {
        return lst1
    }
    if l1 > l2 {
        return lst2
    }
    return lst1
}



