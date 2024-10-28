    sort.Ints(l1)
    sort.Ints(l2)
    m1 := make(map[int]int)
    for _, v := range l1 {
        m1[v]++
    }
    for _, v := range l2 {
        m1[v]++
    }
    var com []int
    for k, v := range m1 {
        if v == 2 {
            com = append(com, k