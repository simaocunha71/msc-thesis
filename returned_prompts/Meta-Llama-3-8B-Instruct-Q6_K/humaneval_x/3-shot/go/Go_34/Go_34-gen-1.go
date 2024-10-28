    var result []int
    for _, v := range l {
        found := false
        for _, v2 := range result {
            if v == v2 {
                found = true
                break
            }
        }
        if !found {
            result = append(result, v)
        }
    }
    sort.Ints(result)
    return result
} 



