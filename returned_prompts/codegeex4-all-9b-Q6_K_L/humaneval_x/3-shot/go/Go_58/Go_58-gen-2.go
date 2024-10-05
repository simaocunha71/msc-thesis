    var result []int
    var l1Map = make(map[int]bool)
    var l2Map = make(map[int]bool)
    for _, v := range l1 {
        l1Map[v] = true
    }
    for _, v := range l2 {
        l2Map[v] = true
    }
    for k := range l1Map {
        if l2Map[k] {
            result = append(result, k)
        }
    }
    sort.Ints(result)
    return result
}



