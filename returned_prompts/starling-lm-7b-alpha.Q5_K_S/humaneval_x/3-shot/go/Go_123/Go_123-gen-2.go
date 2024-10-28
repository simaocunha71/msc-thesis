    result := make([]int, 0)
    current := n
    visited := make(map[int]bool)
    for {
        if current%2 == 0 {
            current /= 2
        }else {
            current = 3 * current + 1
        }
        if current == 1 {
            break
        }
        if current%2 == 1 {
            visited[current] = true
            result = append(result, current)
        }
    }
    sort.Slice(result, func(i, j int) bool { return result[i] < result[j] })
    return result
}



