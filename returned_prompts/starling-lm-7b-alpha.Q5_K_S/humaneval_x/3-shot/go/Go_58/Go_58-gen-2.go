    result := make([]int, 0)
    for _, i := range l1 {
        if contains(l2, i) {
            result = append(result, i)
        }
    }
    sort.Ints(result)
    return result
}

func contains(list []int, value int) bool {
    for _, i := range list {
        if i == value {
            return true
        }
    }
    return false
}



