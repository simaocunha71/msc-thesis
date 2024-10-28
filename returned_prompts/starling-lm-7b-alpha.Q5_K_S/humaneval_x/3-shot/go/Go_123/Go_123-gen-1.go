    result := make([]int, 0)
    current := n
    for current > 1 {
        if current % 2 != 0 {
            result = append(result, current)
        }
        if current % 2 == 0 {
            current /= 2
        }else {
            current = 3*current + 1
        }
    }
    sort.Ints(result)
    return result
}




