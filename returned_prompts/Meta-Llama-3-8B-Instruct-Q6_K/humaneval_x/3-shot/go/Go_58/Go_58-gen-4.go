    set1 := make(map[int]bool)
    set2 := make(map[int]bool)
    for _, item := range l1 {
        set1[item] = true
    }
    for _, item := range l2 {
        set2[item] = true
    }

    var result []int
    for k := range set1 {
        if set2[k] {
            result = append(result, k)
        }
    }
    sort.Ints(result)
    return result
}  // 1. Convert the list to a set for each list.
// 2. Find common elements by iterating through the set of one list and checking if the elements are also in the set of the other list.
// 3. Convert the result back to a list and sort it.