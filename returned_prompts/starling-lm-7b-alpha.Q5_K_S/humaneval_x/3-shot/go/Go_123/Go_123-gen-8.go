    result := make([]int, 0)
    current := n
    visited := make(map[int]bool)

    for current != 1 {
        if current % 2 == 0 {
            current = current / 2
        }else {
            current = current * 3 + 1
        }

        if current % 2 != 0 {
            result = append(result, current)
        }
        if visited[current] {
            break
        }
        visited[current] = true
    }

    sort.Slice(result, func(i int, j int) bool {
        return result[i] < result[j]
    })

    return result
}



