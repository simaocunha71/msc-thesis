    l1,l2 := len(lst1),len(lst2)
    if l1<l2 {
        return lst1
    }
    if l1>l2 {
        return lst2
    }
    for i,v := range lst1 {
        if len(v)>len(lst2[i]) {
            return lst2
        }
    }
    return lst1
}



