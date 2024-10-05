    result := make([]int, 0)
    current := n
    seen := make(map[int]bool)

    for current != 1 {
        if current % 2 == 0 {
            current = current / 2
        } else {
            current = 3 * current + 1
        }
        if current % 2 == 1 {
            result = append(result, current)
        }
    }
    sort.Ints(result)
    return result
}



