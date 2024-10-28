    result := make([]int, 0)
    map1 := make(map[int]bool)
    map2 := make(map[int]bool)

    for _,num := range l1{
        map1[num] = true
    }

    for _,num := range l2{
        if _,ok := map1[num];ok{
            map2[num] = true
        }
    }

    for k,_ := range map2{
        result = append(result,k)
    }

    sort.Ints(result)
    return result
}



