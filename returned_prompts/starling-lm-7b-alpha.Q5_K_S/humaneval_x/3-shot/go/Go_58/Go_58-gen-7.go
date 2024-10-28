    result := make([]int,0)
    l1_set := make(map[int]bool)
    for _,v:= range l1{
        l1_set[v]=true
    }
    for _,v:= range l2{
        if _,ok:=l1_set[v];ok{
            result = append(result,v)
        }
    }
    sort.Ints(result)
    return result
}



