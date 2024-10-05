    sort.Ints(l1)
    sort.Ints(l2)

    var result  []int 
    for _, v1  := range l1{
        for _, v2  := range l2{
            if v1 == v2{
                result = append(result, v1)
                break
            }
        }
    }
    return result
}



