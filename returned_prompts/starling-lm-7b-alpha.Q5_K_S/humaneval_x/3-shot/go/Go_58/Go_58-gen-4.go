    result := make(map[int]struct{})
    for _, v := range l1 {
        result[v] = struct{}{}
    }

    intersection := []int{}
    for _, v := range l2 {
        if _, ok := result[v]; ok {
            intersection = append(intersection, v)
        }
    }
    sort.Ints(intersection)
    return intersection
}



