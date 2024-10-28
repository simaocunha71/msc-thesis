    m := make(map[int]bool)
    result := make([]int, 0)

    for _, num := range l1 {
        m[num] = true
    }
    for _, num := range l2 {
        if m[num] {
            result = append(result, num)
        }
    }
    sort.Ints(result)
    return result
}



