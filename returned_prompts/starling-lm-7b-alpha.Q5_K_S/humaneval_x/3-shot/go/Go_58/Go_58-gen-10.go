    result := make([]int,0)
    m := make(map[int]int)
    for _,i := range l1 {
        m[i] = 1
    }
    for _,i := range l2 {
        if _,ok := m[i];ok {
            result = append(result,i)
        }
    }
    sort.Ints(result)
    return result
}



