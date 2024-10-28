    result := make([]int, 0)

    for i := 0; i < n; i++ {
        next_level_stones := n + 1
        if (n % 2 == 0) {
            next_level_stones += 1
        }
        result = append(result, next_level_stones)
        n = next_level_stones
    }
    return result
}



