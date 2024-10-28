    result := make([]int, 0)
    current := n
    for current != 1 {
        if current % 2 == 1 {
            result = append(result, current)
        }
        current = int(math.Floor(float64(current) / 2))
        if current % 2 == 0 {
            current += 1
        }
    }
    sort.Ints(result)
    return result
}



